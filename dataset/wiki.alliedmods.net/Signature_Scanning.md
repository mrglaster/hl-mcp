# Signature Scanning
From AlliedModders Wiki
Jump to: [navigation](https://wiki.alliedmods.net/Signature_Scanning#mw-head), [search](https://wiki.alliedmods.net/Signature_Scanning#p-search)
  

## Contents
  * [1 Introduction](https://wiki.alliedmods.net/Signature_Scanning#Introduction)
  * [2 What is Sigscanning?](https://wiki.alliedmods.net/Signature_Scanning#What_is_Sigscanning.3F)
  * [3 Assembly and Memory](https://wiki.alliedmods.net/Signature_Scanning#Assembly_and_Memory)
  * [4 Before We Go Further](https://wiki.alliedmods.net/Signature_Scanning#Before_We_Go_Further)
  * [5 Scanning for Signatures at Run-time](https://wiki.alliedmods.net/Signature_Scanning#Scanning_for_Signatures_at_Run-time)
    * [5.1 sigscan.h](https://wiki.alliedmods.net/Signature_Scanning#sigscan.h)
    * [5.2 sigscan.cpp](https://wiki.alliedmods.net/Signature_Scanning#sigscan.cpp)
  * [6 Finding the Signature of a Function](https://wiki.alliedmods.net/Signature_Scanning#Finding_the_Signature_of_a_Function)
    * [6.1 Linux](https://wiki.alliedmods.net/Signature_Scanning#Linux)
    * [6.2 Windows](https://wiki.alliedmods.net/Signature_Scanning#Windows)
  * [7 Creating a Searchable Signature](https://wiki.alliedmods.net/Signature_Scanning#Creating_a_Searchable_Signature)
    * [7.1 sigcreator.c](https://wiki.alliedmods.net/Signature_Scanning#sigcreator.c)
    * [7.2 makesig.idc (IDA)](https://wiki.alliedmods.net/Signature_Scanning#makesig.idc_.28IDA.29)
  * [8 Contributors](https://wiki.alliedmods.net/Signature_Scanning#Contributors)
  * [9 References](https://wiki.alliedmods.net/Signature_Scanning#References)
  * [10 See Also](https://wiki.alliedmods.net/Signature_Scanning#See_Also)


## Introduction
This article demonstrates a technique developed by Lance Vorgin known as "Signature Scanning", or sigscanning for short. 
## What is Sigscanning?
Sigscanning is a multi-step process involving extracting function signatures from a binary and then scanning for them at run-time to locate an otherwise-hidden function. A signature for a function is a set of bytes unique to a function. These bytes are the instructions a program uses to operate. These sets of bytes are what make up functions (or subroutines as they are called in Assembly). When we have enough of these bytes to form a unique set, we can then match them again to the function in memory. 
Why is this useful for plugins? Each time Valve releases an update for their mods, they may change classes such as CBaseEntity used by many plugin coders to interact with a player’s entity. Due to the fact that we do not have the appropriate class headers for each of these changes, we may be using virtual functions that now exist at different addresses. This would cause a crash at run-time. To avoid this, the following solutions are available: 
  * rely on manual offsets into the class' vtable
  * modify the provided class headers by inserting dummy virtual functions to fix the offsets
  * sigscanning


Each have their pros and cons, but it turns out that although sigscanning is the most tedious out of the three, it is the most reliable. The first two choices are typically broken by updates. 
## Assembly and Memory
To understand all of this, one must first understand how the code of a C++ program is compiled into a binary file. 
When you hit "Build Solution" on your IDE or run a makefile, your compiler does a multitude of operations. First it takes the code and runs it through a preprocessor. The preprocessor takes all the "#" directives (e.g. #define, #include, etc.) and substitutes them with normal C++ code. After the preprocessor has done its job, the code is passed on to the parser. In simplified terms, the parser basically takes C++ code and turns it into Assembly (asm) code. After the parser has parsed the code into Assembly code, the assembler "assembles" the code into mostly machine (byte) code which is put into object files that carry the .obj or .o extension. Then the linker gathers all the object files where it looks for function calls and sets the "links" to them (static linking) as well as external calls to functions outside the scope of the assembled code (dynamic linking) and finally maps any runtime calls (runtime linking). After this, it finally outputs the finished product (a binary file, i.e. an executable or library). When a server loads your plugin, it uses runtime calls to call functions from within your plugin, and likewise your plugin calls functions from the server. 
Now where this all comes into play in sigscanning is where you will be taking the server module (.dll or .so file) from memory and scanning it in its machine-code form for those functions that you need. This is done by first disassembling the server module back into Assembly form and finding the instructions that make up that function you want. 
Assembly is the "lowest-level" language in programming terms. It is easy to flip-flop between Assembly and machine code because they are basically the same, except Assembly uses something called "Mnemonics" before every instruction. These are the human-readable keywords _push_ , _pop_ , _mov_ , _call_ , etc. that define what the instruction does. As C++ code is translated into Assembly, you can imagine the very structured syntax of C++ flattened out into primitive simple Assembly instructions. I won’t go into further detail on Assembly due to its complex nature. The best way to learn more about it (which is recommended) is to read one of the reference links provided at the bottom of this writing. 
## Before We Go Further
Read BAILOPAN’s three DevLogs on sigscanning to gain an understanding of the proceeding sections. 
  * _Oh, you’ve not hacked yet?_ – <http://www.sourcemod.net/devlog/?p=55>
  * _Finding Functions, Part 2_ – <http://www.sourcemod.net/devlog/?p=56>
  * _Finding Functions, Part 3_ – <http://www.sourcemod.net/devlog/?p=57>


## Scanning for Signatures at Run-time
This is the complete code for a basic sigscanner. All functions and variables are described with comments. 
### sigscan.h
```
#ifndef SIGSCAN_H
#define SIGSCAN_H
 
class CSigScan {
private:
    /* Private Variables */
    /* Base Address of the server module in memory */
    static unsigned char *base_addr;
    /* The length to the module's ending address */
    static size_t base_len;
 
    /* The signature to scan for */
    unsigned char *sig_str;
    /* A mask to ignore certain bytes in the signature such as addresses
       The mask should be as long as all the bytes in the signature string
       Use '?' to ignore a byte and 'x' to check it
       Example: "xxx????xx" - The first 3 bytes are checked, then the next 4 are
       ignored, then the last 2 are checked */
    char *sig_mask;
    /* The length of sig_str and sig_mask (not including a terminating null for sig_mask) */
    size_t sig_len;
 
    /* Private Functions */
    void* FindSignature(void);
 
public:
    /* Public Variables */
 
    /* sigscan_dllfunc is a pointer of something that resides inside the gamedll so we can get
       the base address of it. From a SourceMM plugin, just set this to ismm->serverFactory(0)
       in Load(). From a Valve Server Plugin, you must set this to an actual factory returned
       from gameServerFactory and hope that a SourceMM plugin did not override it. */
    static void *(*sigscan_dllfunc)(const char *pName, int *pReturnCode);
 
    /* If the scan was successful or not */
    char is_set;
    /* Starting address of the found function */
    void *sig_addr;
 
    /* Public Functions */
    CSigScan(void): sig_str(NULL), sig_mask(NULL), sig_len(0), sig_addr(NULL) {}
    ~CSigScan(void);
 
    static bool GetDllMemInfo(void);
    void Init(unsigned char *sig, char *mask, size_t len);
};
 
/* Sigscanned member functions are casted to member function pointers of this class
   and called with member function pointer syntax */
class EmptyClass { };
 
void InitSigs(void);
 
/* Sig Functions */
class CBaseAnimating;
void CBaseAnimating_Ignite(CBaseAnimating *cba, float flFlameLifetime);
 
#endif
```

### sigscan.cpp
```
#include <stdio.h>
 
#ifdef WIN32
    #define WIN32_LEAN_AND_MEAN
    #include <windows.h>
#else
    #include <dlfcn.h>
    #include <sys/types.h>
    #include <sys/stat.h> 
#endif
 
#include "sigscan.h"
 
/* There is no ANSI ustrncpy */
unsigned char* ustrncpy(unsigned char *dest, const unsigned char *src, int len) {
    while(len--)
        dest[len] = src[len];
 
    return dest;
}
 
/* //////////////////////////////////////
    CSigScan Class
    ////////////////////////////////////// */
unsigned char* CSigScan::base_addr;
size_t CSigScan::base_len;
void *(*CSigScan::sigscan_dllfunc)(const char *pName, int *pReturnCode);
 
/* Initialize the Signature Object */
void CSigScan::Init(unsigned char *sig, char *mask, size_t len) {
    is_set = 0;
 
    sig_len = len;
    sig_str = new unsigned char[sig_len];
    ustrncpy(sig_str, sig, sig_len);
 
    sig_mask = new char[sig_len+1];
    strncpy(sig_mask, mask, sig_len);
    sig_mask[sig_len+1] = 0;
 
    if(!base_addr)
        return ; // GetDllMemInfo() Failed
 
    if((sig_addr = FindSignature()) == NULL)
        return ; // FindSignature() Failed
 
    is_set = 1;
    // SigScan Successful!
}
 
/* Destructor frees sig-string allocated memory */
CSigScan::~CSigScan(void) {
    delete[] sig_str;
    delete[] sig_mask;
}
 
/* Get base address of the server module (base_addr) and get its ending offset (base_len) */
bool CSigScan::GetDllMemInfo(void) {
    void *pAddr = (void*)sigscan_dllfunc;
    base_addr = 0;
    base_len = 0;
 
    #ifdef WIN32
    MEMORY_BASIC_INFORMATION mem;
 
    if(!pAddr)
        return false; // GetDllMemInfo failed!pAddr
 
    if(!VirtualQuery(pAddr, &mem, sizeof(mem)))
        return false;
 
    base_addr = (unsigned char*)mem.AllocationBase;
 
    IMAGE_DOS_HEADER *dos = (IMAGE_DOS_HEADER*)mem.AllocationBase;
    IMAGE_NT_HEADERS *pe = (IMAGE_NT_HEADERS*)((unsigned long)dos+(unsigned long)dos->e_lfanew);
 
    if(pe->Signature != IMAGE_NT_SIGNATURE) {
        base_addr = 0;
        return false; // GetDllMemInfo failedpe points to a bad location
    }
 
    base_len = (size_t)pe->OptionalHeader.SizeOfImage;
 
    #else
 
    Dl_info info;
    struct stat buf;
 
    if(!dladdr(pAddr, &info))
        return false;
 
    if(!info.dli_fbase || !info.dli_fname)
        return false;
 
    if(stat(info.dli_fname, &buf) != 0)
        return false;
 
    base_addr = (unsigned char*)info.dli_fbase;
    base_len = buf.st_size;
    #endif
 
    return true;
}
 
/* Scan for the signature in memory then return the starting position's address */
void* CSigScan::FindSignature(void) {
    unsigned char *pBasePtr = base_addr;
    unsigned char *pEndPtr = base_addr+base_len;
    size_t i;
 
    while(pBasePtr < pEndPtr) {
        for(i = 0;i < sig_len;i++) {
            if((sig_mask[i] != '?') && (sig_str[i] != pBasePtr[i]))
                break;
        }
 
        // If 'i' reached the end, we know we have a match!
        if(i == sig_len)
            return (void*)pBasePtr;
 
        pBasePtr++;
    }
 
    return NULL;
}
 
/* Signature Objects */
CSigScan CBaseAnimating_Ignite_Sig;
 
/* Set the static base_addr and base_len variables then initialize all Signature Objects */
void InitSigs(void) {
    CSigScan::GetDllMemInfo();
 
    /* void CBaseAnimating::Ignite(float flFlameLifetime, bool bNPCOnly, float flSize,
        bool bCalledByLevelDesigner);
    Last Address: 0x220BC7A0
    Signature: 56  8B  F1  8B? 86? BC? 00? 00? 00? C1? E8? 1B? A8? 01? 0F? 85?
           9A? 00? 00? 00? 8B  16  FF  92? F0? 00? 00? 00? 80? 7C? 24? 0C?
           00? 74? 08? 84  C0  0F? 84? 83? 00? 00? 00? 3C  01  75? 20? 80
           7C  24  14  00  75? 19? 8B  CE  E8  83? 1A? 01? 00? 85? C0? 74?
           0E? 8B  10  8B  C8  FF  92? 08? 05? 00? 00? 84  C0  74? 5F? 57
           6A  01  56  E8  48? EA? 07? 00? 8B  F8  83  C4  08  85  FF  74?
           3D? 8B  44  24  0C  50  8B  CF  E8  83? E5? 07? 00? 68  00  00
           00  08  8B  CE
    */
    CBaseAnimating_Ignite_Sig.Init((unsigned char*)
    "\x56\x8B\xF1\x8B\x86\xBC\x00\x00\x00\xC1\xE8\x1B\xA8\x01\x0F\x85\x9A\x00\x00\x00"
    "\x8B\x16\xFF\x92\xF0\x00\x00\x00\x80\x7C\x24\x0C\x00\x74\x08\x84\xC0\x0F\x84\x83"
    "\x00\x00\x00\x3C\x01\x75\x20\x80\x7C\x24\x14\x00\x75\x19\x8B\xCE\xE8\x83\x1A\x01"
    "\x00\x85\xC0\x74\x0E\x8B\x10\x8B\xC8\xFF\x92\x08\x05\x00\x00\x84\xC0\x74\x5F\x57"
    "\x6A\x01\x56\xE8\x48\xEA\x07\x00\x8B\xF8\x83\xC4\x08\x85\xFF\x74\x3D\x8B\x44\x24"
    "\x0C\x50\x8B\xCF\xE8\x83\xE5\x07\x00\x68\x00\x00\x00\x08\x8B\xCE"
    ,
    "xxx?????????????????"
    "xxx????????????xx???"
    "???xx??xxxxx??xxx???"
    "?????xxxxx?????xx??x"
    "xxxx????xxxxxxx??xxx"
    "xxxxx????xxxxxxx"
    ,
    116);
 
    return ;
}
 
/* Example of a sig-scanned method function */
void CBaseAnimating_Ignite(CBaseAnimating *cba, float flFlameLifetime) {
    int bNPCOnly = false, bCalledByLevelDesigner = false;
    float flSize = 0.0f;
 
    if(!CBaseAnimating_Ignite_Sig.is_set)
        return ; // sigscan failed
 
    union {
        void (EmptyClass::*mfpnew)(float, bool, float, bool);
        void* addr;
    } u;
    u.addr = CBaseAnimating_Ignite_Sig.sig_addr;
 
    (reinterpret_cast<EmptyClass*>(cba)->*u.mfpnew)(flFlameLifetime, (bool)bNPCOnly, flSize,
        (bool)bCalledByLevelDesigner);
 
    return;
}
```

This will find the signature of a function at runtime, however it is useless unless you already have or know how to find signatures for which it can scan. 
## Finding the Signature of a Function
To find a signature for a function, we need a Disassembler to disassemble the server module. Here are links to free Disassemblers that seem to work well: 
  * [IDA Pro Freeware Version (Windows)](http://www.hex-rays.com/idapro/idadownfreeware.htm)
  * [PEBrowse Professional (Windows)](http://www.smidgeonsoft.prohosting.com/pebrowse-pro-file-viewer.html)
  * [Proview “PVDasm” Disassembler (Windows)](http://pvdasm.reverse-engineering.net/index.php?Section=1)
  * [GNU objdump (Linux)](http://www.gnu.org/software/binutils/manual/html_chapter/binutils_4.html)
  * [Data Display Debugger (Linux)](http://www.gnu.org/software/ddd/)


### Linux
Showdax pointed out a very helpful way that makes finding signatures under Linux much easier than under Windows. The GNU tool "objdump" can be used against the server module to disassemble the binary into AT&T Assembly code with each subroutine given its name from the source code. Here is an example of how to use the objdump tool: 
```
~/usr/srcds/dod/bin$ objdump -d server_i486.so > server_i486.so.objdump
```

This dumps the disassembled code into the file "server_i486.so.objdump". You can then simply open up that file and search for the function name that corresponds to its subroutine then extract its bytes to create a signature (discussed later in [#Creating a Searchable Signature](https://wiki.alliedmods.net/Signature_Scanning#Creating_a_Searchable_Signature)). 
### Windows
Under Windows, finding a signature becomes much more complicated as PE-format binaries do not include symbol names for each subroutine. I suggest using the IDA Pro Freeware Disassembler since I will be using a method I have found to find signatures that I only know how to do in IDA Pro (although you may be able to find a way to do my method in the other disassemblers). 
The rest of this section will assume you are running Windows, have a copy of Microsoft Visual Studio C++ and are using the IDA Pro Freeware Disassembler. First what you need to do is compile the HL2:DM server module. So navigate your way to the "hl2src/dlls" directory and open up "hl_sdk.vcproj". Once open inside MSVC++, go to the Build menu and select Configuration Manager. Set the configuration to "Release" and press OK. Go to the Build menu again and select Build. This may take a bit as everything is compiled together. Once finished, you should have a new directory named "Release_hl2." Inside, there will be the compiled server.dll file and a server.pdb file. The PDB file is key to finding the subroutines in Assembly for the function you want to use. 
Now open IDA Pro and go to the File menu and open the server.dll file you just compiled. When you open it, a dialog will pop up. Just press "OK" and everything will start to load. Eventually IDA Pro will say something akin to "There is a PDB file located in the same directory for this binary." Click "Yes" and it will use that PDB file to name the subroutines which will make this process much easier. As things load, IDA Pro will go through the DLL, disassembling it and naming everything to their corresponding function or variable name. This may take a while and may even appear that IDA has frozen, but it has not so don't close it or you will have to start over. 
After some time, everything will have finished. Before we continue, however, we have to open up yet another IDA Pro again (don't close the other IDA Pro) and load the server.dll for the mod we will be sigscanning (in this case, Counter-Strike: Source). This file is located in "cstrike/bin" in your game installation directory. Again, do the same procedure, except this time we won't have a PDB file for it. This should take a shorter time than last time since there is no PDB file. After both IDA Pro processes have finished disassembling, we are ready to start finding signatures. 
To start looking for a signature, switch over to the HL2:DM server module IDA Pro window. Above, we have the signature for CBaseAnimating::Ignite in the [#sigscan.cpp](https://wiki.alliedmods.net/Signature_Scanning#sigscan.cpp) section. As a new example, let's try to find the signature for Teleporting an entity. This is the prototype for its method from the source code: 
```
virtual void CBaseEntity::Teleport(const Vector *newPosition, const QAngle *newAngles,
    const Vector *newVelocity);
```

Now in IDA Pro look for _CBaseEntity::Teleport_ in the _Names_ list then double click it. You should be brought to the location of _CBaseEntity::Teleport_ in the disassembly, however, its internal name is given as _CBaseEntity_Teleport_. As you can see, IDA Pro lists all the local and parameter variables near the top (lines starting with _var__ and _arg__), and then the actual code is listed below with its corresponding byte representation. (Tip: I had to actually set IDA Pro to list the opcode bytes from the Options menu, in "General" then under the tab "Disassembly"). At first, it seems feasible to just use the bytes here for the signature, but Valve decided to change almost all the CBase* methods (that I've seen) for Counter-Strike: Source from the Half-Life 2: Deathmatch code. Due to this fact, we will have to use the HL2:DM disassembly as clues for finding the same function/method in the CS:S disassembly. To find our Teleport function, we will have to find a unique set of instructions that wouldn't be repeated in another subroutine. I had to do some trial and error with this function since Valve had changed or moved various pieces of code. If you try looking over the subroutine for something unique, you may see a group of repeated _mov_ instructions: 
```
.text:220C96CF 89 44 24 18          mov   [esp+30h+var_18], eax
.text:220C96D3 89 74 24 1C          mov   [esp+30h+var_14], esi
.text:220C96D7 89 74 24 20          mov   [esp+30h+var_10], esi
.text:220C96DB 89 74 24 24          mov   [esp+30h+var_C], esi
.text:220C96DF 89 74 24 28          mov   [esp+30h+var_8], esi
.text:220C96E3 89 74 24 2C          mov   [esp+30h+var_4], esi
```

Try searching for part of this in the CS:S disassembly. If you get results, search for the next item to make sure there isn't another set of the same instructions. Then to verify this is the correct subroutine for the function Teleport(), compare the two subroutines to see if they have similar instructions in the same places. If they do then it is most likely correct and now you can use some of the instructions from your find in machine-code form to create a signature, which is discussed in the next section. 
## Creating a Searchable Signature
Once we have found the subroutine for the function we want, we can start extracting the bytes for use in a signature. Here is part of the assembly for _CBaseEntity::Teleport_ : 
```
220D9940                     CBaseEntity_Teleport proc near          ; CODE XREFsub_220B6330+14 p
220D9940                                                             ; sub_22143900+A p ...
220D9940
220D9940 83 EC 18            sub     esp, 18h
220D9943 53                  push    ebx
220D9944 56                  push    esi
220D9945 8B D9               mov     ebx, ecx
220D9947 8B 0D 78 B2 46 22   mov     ecx, dword_2246B278
220D994D 33 F6               xor     esi, esi
220D994F 33 C0               xor     eax, eax
220D9951 3B CE               cmp     ecx, esi
220D9953 7E 21               jle     short loc_220D9976
220D9955 8B 15 6C B2 46 22   mov     edx, dword_2246B26C
220D995B EB 03               jmp     short loc_220D9960
220D995B                     ; ---------------------------------------------------------------------------
220D995D 8D 49 00            align 10h
220D9960
220D9960                     loc_220D9960                          ; CODE XREFCBaseEntity_Teleport+1B j
220D9960                                                             ; CBaseEntity_Teleport+2A j
220D9960 39 1C 82            cmp     [edx+eax*4], ebx
220D9963 74 09               jz      short loc_220D996E
220D9965 83 C0 01            add     eax, 1
220D9968 3B C1               cmp     eax, ecx
220D996A 7C F4               jl      short loc_220D9960
220D996C EB 08               jmp     short loc_220D9976
220D996E                     ; ---------------------------------------------------------------------------
220D996E
220D996E                     loc_220D996E                          ; CODE XREFCBaseEntity_Teleport+23 j
220D996E 3B C6               cmp     eax, esi
220D9970 0F 8D 17 01 00 00   jge     loc_220D9A8D
220D9976
220D9976                     loc_220D9976                          ; CODE XREFCBaseEntity_Teleport+13 j
220D9976                                                             ; CBaseEntity_Teleport+2C j
220D9976 55                  push    ebp
220D9977 57                  push    edi
220D9978 8D 44 24 10         lea     eax, [esp+28h+var_18]
220D997C 50                  push    eax
220D997D 51                  push    ecx
220D997E B9 6C B2 46 22      mov     ecx, offset dword_2246B26C
220D9983 89 5C 24 18         mov     [esp+30h+var_18], ebx
220D9987 E8 B4 88 F9 FF      call    sub_22072240
220D998C 8D 4C 24 14         lea     ecx, [esp+28h+var_14]
220D9990 51                  push    ecx
220D9991 53                  push    ebx
220D9992 89 44 24 18         mov     [esp+30h+var_18], eax
220D9996 89 74 24 1C         mov     [esp+30h+var_14], esi
220D999A 89 74 24 20         mov     [esp+30h+var_10], esi
```

I have written a small C program for which I use to create a signature string and signature mask from. It is not necessary to use, but it can help to reduce the amount of tedious work you have to do to create a signature. 
### sigcreator.c
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
 
int main() {
    int i, len, out_i = 0, mask_i = 0;
    char *sig, *out, *mask;
 
    sig = (char*)calloc(1024, sizeof(char));
 
    printf("?");
    fgets(sig, 1022, stdin);
    len = strlen(sig);
 
    out = (char*)calloc(len*2, sizeof(char));
    mask = (char*)calloc(len*2, sizeof(char));
 
    for(i = 0;i < len;i++) {
        if(isalnum(sig[i]) && isalnum(sig[i+1])) {
            out[out_i++] = '\\';
            out[out_i++] = 'x';
            out[out_i++] = sig[i];
            out[out_i++] = sig[i+1];
            if(sig[i+2] == '?') {
                mask[mask_i++] = '?';
                i += 2;
            }
            else {
                mask[mask_i++] = 'x';
                i++;
            }
        }
    }
 
    printf("\n\nSize%d\n\nSig:\n%s\n\nMask:\n%s", strlen(mask), out, mask);
    getchar();
 
    free(sig);
    free(out);
    free(mask);
    return 0;
}
```

It takes an input string of hexadecimal characters just as they appear in bold in the Assembly above. For each byte that should be ignored, a question mark after a hexadecimal byte will tell the program where a "?" should be in the signature mask. I will give an example of what the input and output should look like near the end of this section. 
When creating a signature, you must also create a signature mask as well. A signature mask tells the sigscanner which bytes to ignore, such as addresses which may change at runtime. The signature mask is the same length as the signature. A question mark ("?") in the mask signifies the position of the byte in the signature string to be ignored. Any other character corresponding to a byte in the signature string will be checked (usually we use "x" to represent these). 
For the Teleport() function we found in the last section, we will build our signature from the bold hexadecimal characters in the Assembly above. I will be using the format of my "Sig Creator" for developing a signature string and mask for the sigscanner. The first three instructions in the subroutine are called the "function prologue." These instructions will most likely never change as long as the variable declarations are not changed. So to start off, input "83 EC 18 53 56" into the sigcreator. Next is a mov instruction that probably won’t change "8B D9". After that is another mov instruction, but this mov instruction contains an address in it, so add this to the input "8B? 0D? 78? B2? 46? 22?". This will appear as question marks in the signature mask. The next set of xor instructions don’t reference an address so they’re safe to add normally to the input "33 F6 33 C0". From here on, continue to input each segment of bytes into the sigcreator, where any segment referencing an address should have question marks following each hexadecimal character pairs (like I did for the mov instruction). Eventually you’ll end at those last mov instructions. This isn’t the end of the subroutine, but it’s enough to develop a worthy signature. So press enter in the sigcreator, and it should output something like this: 
```
?83 EC 18 53 56 8B D9 8B? 0D? 78? B2? 46? 22? 33 F6 33 C0 3B CE 7E? 21? 8B? 15?
6C? B2? 46? 22? EB? 03? 8D? 49? 00? 39 1C 82 74? 09? 83? C0? 01? 3B C1 7C? F4?
EB? 08? 3B C6 0F? 8D? 17? 01? 00? 00? 55 57? 8D? 44? 24? 10? 50 51 B9? 6C? B2?
46? 22? 89 5C 24 18 E8? B4? 88? F9? FF? 8D? 4C? 24? 14? 51 53 89 44 24 18 89
74 24 1C 89 74 24 20 89 74 24 24 89 74 24 28 89 74 24 2C


Size106

Sig:
\x83\xEC\x18\x53\x56\x8B\xD9\x8B\x0D\x78\xB2\x46\x22\x33\xF6\x33\xC0\x3B\xCE\x7E
\x21\x8B\x15\x6C\xB2\x46\x22\xEB\x03\x8D\x49\x00\x39\x1C\x82\x74\x09\x83\xC0\x01
\x3B\xC1\x7C\xF4\xEB\x08\x3B\xC6\x0F\x8D\x17\x01\x00\x00\x55\x57\x8D\x44\x24\x10
\x50\x51\xB9\x6C\xB2\x46\x22\x89\x5C\x24\x18\xE8\xB4\x88\xF9\xFF\x8D\x4C\x24\x14
\x51\x53\x89\x44\x24\x18\x89\x74\x24\x1C\x89\x74\x24\x20\x89\x74\x24\x24\x89\x74
\x24\x28\x89\x74\x24\x2C

Mask:
xxxxxxx??????xxxxxx?????????????xxx?????xx????xx??????x?????xx?????xxxx?????????
xxxxxxxxxxxxxxxxxxxxxxxxxx
```

Now you have a nice signature and mask you can use for your sigscanner and it also gives you the length of the signature as well. Cheers! 
### makesig.idc (IDA)
The SourceMod repository has [a more recent script named makesig.idc](https://github.com/alliedmodders/sourcemod/blob/master/tools/ida_scripts/makesig.idc) that automatically builds [a SourceMod-ready signature](https://wiki.alliedmods.net/SDKTools_\(SourceMod_Scripting\)#Signature_Scans "SDKTools \(SourceMod Scripting\)") given a function. The script works as of the freeware version of IDA 7.0 (after replacing every reference of "dtyp" with "dtype"). 
Once you've found your subroutine in IDA, load the script file; once the script is done running you should (hopefully) get a display of the bytes and the wildcarded signature in the program's output window. 
## Contributors
Thank you to those who contributed to this document directly and/or indirectly: 
  * Lance Vorgin – Forefather of sigscanners, posted his sigscanner on the [SourceMod](https://wiki.alliedmods.net/SourceMod "SourceMod") forums somewhere
  * BAILOPAN – Created his DevLogs on how to create a sigscanner, also gave tips as well as other useful information
  * Showdax – Suggested the objdump command for disassembly on Linux
  * CyberMind – Examples of how to use a different method of calling sig functions
  * Jacob Lojo – Posted a thread on how to develop a signature from disassembly (I was having trouble finding sigs with my scanner before his post). Also contributed a link to another disassembler
  * SeLfkiLL – Revision and completed code for the sigscanner and sigcreator


## References
  * _Oh, you’ve not hacked yet?_ – <http://www.sourcemod.net/devlog/?p=55>
  * _Finding Functions, Part 2_ – <http://www.sourcemod.net/devlog/?p=56>
  * _Finding Functions, Part 3_ – <http://www.sourcemod.net/devlog/?p=57>
  * _Introduction to Reverse Engineering Software_ - <http://www.acm.uiuc.edu/sigmil/RevEng/index.html>
  * _The Art of Assembly Language Programming_ - <http://maven.smith.edu/~thiebaut/ArtOfAssembly/artofasm.html>


## See Also
  * [Signatures_and_Offsets](https://wiki.alliedmods.net/index.php?title=Signatures_and_Offsets&action=edit&redlink=1 "Signatures and Offsets \(page does not exist\)")


