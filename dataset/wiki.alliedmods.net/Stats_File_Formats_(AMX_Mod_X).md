# Stats File Formats (AMX Mod X)
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#mw-head), [search](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#p-search)
AMX Mod X has statistics modules for Counter-Strike (CSX), Day of Defeat (DoDX), Team Fortress Classic (TFCX), and The Specialists (TSX). 
They each have their own similar but separate binary file format. These file formats must be sequentially read and written, and are not organized into tables. This makes them a bit confusing to extract iteratively, however the format is still trivial. 
Each stats file has a header, which contains the version. After the header, each stats entry is written sequentially. Each stats entry contains strings, and the strings are prefixed with the number of bytes to read. Once this number contains zero, the stats file has no more data, and thus iteration must be stopped. 
The file formats in this document are displayed as lists. When the list has an indented section, it means that that section of the file is repeated until a condition. Explanations of the data types are below. Sample code is provided for CSX. 
## Contents
  * [1 How to Interpret](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#How_to_Interpret)
  * [2 CSX (csstats.dat)](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#CSX_.28csstats.dat.29)
  * [3 Sample Code for Reading/Writing](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#Sample_Code_for_Reading.2FWriting)
    * [3.1 Perl](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#Perl)
    * [3.2 C#](https://wiki.alliedmods.net/Stats_File_Formats_\(AMX_Mod_X\)#C.23)


# How to Interpret
  * `int8/uint8` - Signed or Unsigned Byte (8 bits). C types: char, unsigned char
  * `int16/uint16` - Signed or Unsigned Word (16 bits). C types: short, unsigned short
  * `int32/uint16` - Signed or Unsigned Doubleword (32 bits). C types: int, unsigned int
  * `sz` - Zero-terminated C-style string


If a size is followed by [N], for example, `int8[9]`, this would mean 9 blocks of int8 data must be read. 
# CSX (csstats.dat)
The CSSTATS format has RANK_VERSION of 11. The version numbers are considered isolated rather than backwards or forward compatible. 
  * `int16` - `RANK_VERSION`
  * `uint16` - Bytes in first string (if 0, no entries) 
    * `sz` - Name (read N bytes, where N is previous uint16)
    * `uint16` - Bytes of next string
    * `sz` - Steam ID (read N bytes, where N is previous uint16)
    * `uint32` - Team kills
    * `uint32` - Damage
    * `uint32` - Deaths
    * `int32` - Kills
    * `uint32` - Shots
    * `uint32` - Hits
    * `uint32` - Headshots
    * `uint32` - Defusions
    * `uint32` - Defusal Attempts
    * `uint32` - Plants
    * `uint32` - Explosions
    * `uint32[9]` - Body Hits (array of ints, one for each body hit area)
    * `uint16` - If zero, end of file. Otherwise, loop back up and read the next name for this many bytes.


# Sample Code for Reading/Writing
## Perl
This example reads in a CSX stats file. Once read, it then demonstrates displaying the contents. You can optionally specify a new file to output the contents to. Insert code in between to change the result set. 
```
#!/usr/bin/perl
 
my $infile = [shift](http://perldoc.perl.org/functions/shift.html);
my $outfile = [shift](http://perldoc.perl.org/functions/shift.html);
my @players;
my $buffer;
my $RANK_VERSION = 11;
 
[die](http://perldoc.perl.org/functions/die.html)("Usage: ./statsed.pl <infile> [outfile]\n") unless $infile ne "";
 
[open](http://perldoc.perl.org/functions/open.html)(INFILE, $infile) or [die](http://perldoc.perl.org/functions/die.html) "File $infile could not be opened.\n";
[binmode](http://perldoc.perl.org/functions/binmode.html)(INFILE);
 
if (![read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 2))
{
	[die](http://perldoc.perl.org/functions/die.html) "File $infile looks like an invalid file.\n";
	[close](http://perldoc.perl.org/functions/close.html)(INFILE);
}
 
my $vers = [unpack](http://perldoc.perl.org/functions/unpack.html)("s1", $buffer);
if ($vers != $RANK_VERSION)
{
	[print](http://perldoc.perl.org/functions/print.html) "File $infile does not have the correct header version ($RANK_VERSION)\n";
	[die](http://perldoc.perl.org/functions/die.html)("Detected version: $vers\n");
}
 
if (![read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 2))
{
	[die](http://perldoc.perl.org/functions/die.html) "File $infile looks malformed.\n";
}
 
my $bytes = [unpack](http://perldoc.perl.org/functions/unpack.html)("S1", $buffer);
my $num = 0;
my $str = "";
my @stats;
 
#INPUT FILE
while ($bytes)
{
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, $bytes);
	$players[$num]->{name} = [unpack](http://perldoc.perl.org/functions/unpack.html)("Z*", $buffer);
 
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 2);
	$bytes = [unpack](http://perldoc.perl.org/functions/unpack.html)("S1", $buffer);
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, $bytes);
	$players[$num]->{auth} = [unpack](http://perldoc.perl.org/functions/unpack.html)("Z*", $buffer);
 
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 11 * 4);
	@stats = [unpack](http://perldoc.perl.org/functions/unpack.html)("L11", $buffer);
	$players[$num]->{tks} = $stats[0];
	$players[$num]->{damage} = $stats[1];
	$players[$num]->{deaths} = $stats[2];
	$players[$num]->{kills} = $stats[3];
	$players[$num]->{shots} = $stats[4];
	$players[$num]->{hits} = $stats[5];
	$players[$num]->{hs} = $stats[6];
	$players[$num]->{defuses} = $stats[7];
	$players[$num]->{defuse_attempts} = $stats[8];
	$players[$num]->{plants} = $stats[9];
	$players[$num]->{explosions} = $stats[10];
 
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 9*4);
	@{$players[$num]->{hits}} = [unpack](http://perldoc.perl.org/functions/unpack.html)("L9", $buffer);
 
	[read](http://perldoc.perl.org/functions/read.html)(INFILE, $buffer, 2);
	$bytes = [unpack](http://perldoc.perl.org/functions/unpack.html)("S1", $buffer);
 
	$num++;
}
 
[close](http://perldoc.perl.org/functions/close.html)(INFILE);
 
# EXAMPLE CODE
for ($i=0; $i<=$#players; $i++)
{
	my %player = %{$players[$i]};
	my @stats = @{$player{hits}};
	[print](http://perldoc.perl.org/functions/print.html) $player{name} . ", " . $player{auth} . ", ";
	[print](http://perldoc.perl.org/functions/print.html) $player{kills} . ", " . $player{deaths} . ", " . $player{shots} . "\n";
	for ($j=0; $j<9; $j++)
	{
		[print](http://perldoc.perl.org/functions/print.html) "Hit group $j: " . $stats[$j] . "\n";
	}
}
#END EXAMPLE CODE
 
 
#OUTPUT FILE
if ($outfile ne "")
{
	[open](http://perldoc.perl.org/functions/open.html) (OUTFILE, ">$outfile") or [die](http://perldoc.perl.org/functions/die.html)("Could not open output file: $outfile\n");
	[binmode](http://perldoc.perl.org/functions/binmode.html)(OUTFILE);
 
	[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("s1", $RANK_VERSION));
 
	my %player;
	my @stats;
	for ($i=0; $i<=$#players; $i++)
	{
		%player = %{$players[$i]};
		@stats = @{$player{hits}};
 
		[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("S1", ([length](http://perldoc.perl.org/functions/length.html)($player{name})+1) ));
		[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("Z*", $player{name}));
		[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("S1", ([length](http://perldoc.perl.org/functions/length.html)($player{auth})+1) ));
		[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("Z*", $player{auth}));
		[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("L11",
			$player{tks},
			$player{damage},
			$player{deaths},
			$player{kills},
			$player{shots},
			$player{hits},
			$player{hs},
			$player{defuses},
			$player{defuse_attempts},
			$player{plants},
			$player{explosions}));
		for ($j=0; $j<9; $j++)
		{
			[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("L1", $stats[$j]));
		}
	}
 
	[syswrite](http://perldoc.perl.org/functions/syswrite.html)(OUTFILE, [pack](http://perldoc.perl.org/functions/pack.html)("S1", 0));
 
	[close](http://perldoc.perl.org/functions/close.html)(OUTFILE);	
}
```

## C#
The StatsFile.ReadEntriesToList member function below is part of a quick C# class. Note that it uses an ArrayList rather than an Array, since the number of items is not known beforehand. 
```
using System;
using System.Collections;
using System.IO;
using System.Text;
 
public class StatsFile
{
	public const short RANK_VERSION = 11;
 
	public class StatsEntry
	{
		public StatsEntry()
		{
			bodyHits = [new](http://www.google.com/search?q=new+msdn.microsoft.com) uint[9];
		}
 
		public String name;
		public String unique;
		public uint tks;
		public uint damage;
		public uint deaths;
		public int kills;
		public uint shots;
		public uint hits;
		public uint hs;
		public uint bDefusions;
		public uint bDefused;
		public uint bPlants;
		public uint bExplosions;
		public uint [] bodyHits;
	}
 
	public static ArrayList ReadEntriesToList(string file)
	{
		if (!File.Exists(file))
		{
			throw [new](http://www.google.com/search?q=new+msdn.microsoft.com) FileNotFoundException();
		}
 
		System.IO.FileStream stream = File.Open(file, System.IO.FileMode.Open);
 
		if (stream == null)
		{
			throw [new](http://www.google.com/search?q=new+msdn.microsoft.com) FileLoadException();
		}
 
		BinaryReader br = [new](http://www.google.com/search?q=new+msdn.microsoft.com) BinaryReader(stream);
		ArrayList list;
 
		try
		{
			short vers = br.ReadInt16();
 
			if (vers != RANK_VERSION)
			{
				throw [new](http://www.google.com/search?q=new+msdn.microsoft.com) Exception("Bad stats version");
			}
 
			ushort num = br.ReadUInt16();
			list = [new](http://www.google.com/search?q=new+msdn.microsoft.com) ArrayList();
 
			while (num != 0)
			{
				StatsEntry entry = [new](http://www.google.com/search?q=new+msdn.microsoft.com) StatsEntry();
 
				byte [] name = br.ReadBytes(num);
				num = br.ReadUInt16();
				byte [] unique = br.ReadBytes(num);
 
				entry.name = Encoding.ASCII.GetString(name, 0, name.Length-1);
				entry.unique = Encoding.ASCII.GetString(unique, 0, unique.Length-1);
 
				entry.tks = br.ReadUInt32();
				entry.damage = br.ReadUInt32();
				entry.deaths = br.ReadUInt32();
				entry.kills = br.ReadInt32();
				entry.shots = br.ReadUInt32();
				entry.hits = br.ReadUInt32();
				entry.hs = br.ReadUInt32();
				entry.bDefusions = br.ReadUInt32();
				entry.bDefused = br.ReadUInt32();
				entry.bPlants = br.ReadUInt32();
				entry.bExplosions = br.ReadUInt32();
 
				for (int i=0; i<entry.bodyHits.Length; i++)
				{
					entry.bodyHits[i] = br.ReadUInt32();
				}
 
				num = br.ReadUInt16();
 
				list.Add(entry);
			}
		}
		catch 
		{
			throw [new](http://www.google.com/search?q=new+msdn.microsoft.com) FileLoadException("Error reading file");
		}
		finally
		{
			if (br != null)
			{
				br.Close();
				br = null;
			}
			if (stream != null)
			{
				stream.Close();
				stream = null;
			}
		}
 
		return list;
	}
}
```

