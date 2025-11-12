# Half-Life MCP

## Overview

### Introduction

HL-MCP is a specialized MCP (Model Context Protocol) server designed to supercharge your development workflow for AMX Mod X and GoldSrc (Half-Life 1 engine) plugins and mods. Seamlessly integrating with AI-powered IDEs like Cline or Cursor, HL-MCP taps into a curated knowledge base powered by Milvus Lite—a lightweight vector database—to deliver precise, context-aware assistance tailored specifically to the GoldSrc ecosystem. 

---

### Pipeline

<img width="344" height="645" alt="image" src="https://github.com/user-attachments/assets/c209d425-43b5-4e7a-b061-c76b50749ace" />

<br> This system implements a retrieval-augmented generation (RAG) workflow that enables Cursor IDE (etc) to access up-to-date, domain-specific knowledge through semantic search. The pipeline consists of an offline ingestion phase and a runtime inference phase. 
<br>
1. ***Data Ingestion (One-Time or Periodic)*** 
- Data Sources: The process starts with structured or unstructured data from various sources (e.g., documentation, codebases, internal wikis, or public websites).
- Scrapping with Crawl4AI: This component crawls and extracts clean, relevant textual content from the sources.
- Turning text results into vectors with an emmbedding model: The extracted text is processed by an embedding model to convert each document  into a dense vector representation.
- Writing the vectors into Milvus Lite database: The resulting embeddings along with their original text metadata—are stored in Milvus Lite, a lightweight, embedded vector database. This step is typically performed once (or periodically when sources change), not at query time.
     

2. ***Runtime Interaction (On-Demand)*** 

- HL MCP is used as a tool for LLM agent. The tools retrieves valid data search query and returns relevant results. This retrieved content is then injected into the LLM prompt, enabling Cursor to provide accurate, grounded, and domain-aware responses.
Because the vector database is pre-built, query latency remains low, and the system scales efficiently for development-time assistance without reprocessing source data on every request. 

---

### Dataset Overview

The dataset was compiled from a diverse set of community-driven and technical resources related to AMX Mod X and Half-Life modding. The following sources contributed to the dataset, with the number of extracted pages indicated for each:

- **amxx-bg.info**: 2,517 pages  
- **amxmodx.org**: 784 pages  
- **amxxmodx.ru**: 564 pages  
- **wiki.alliedmods.net**: 48 pages  
- **dev-cs.ru**: 15 pages  
- **VipModular Wiki**: 10 pages  
- **aghl.ru**: 10 pages  
- **hlds.run**: 5 pages  
- **amxmodx.ucoz.ru**: 5 pages  
- **GitHub READMEs (selected repositories)**: 4 pages  
- **amx-x.ru**: 2 pages  
- **Other minor sources**: 5 pages  

**Total**: ~3,975 unique pages

This collection captures a broad spectrum of documentation, tutorials, plugin references, and community discussions, making it well-suited for semantic search, retrieval-augmented generation (RAG), or embedding-based applications in the context of legacy modding ecosystems.

---

## Usage 

### Installation 

Follow these steps to set up and configure the project:

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hl-mcp.git
cd hl-mcp
```

#### 2. Configure Environment Variables
Create a `.env` file by copying the example template:
```bash
cp .env.example .env
```

Edit the `.env` file and update the following settings as needed:

```env
# Milvus Settings
MILVUS_URI="/path/to/db-file"                 # Path to your local Milvus database file
MILVUS_COLLECTION_NAME="valve"                # Name of the Milvus collection to use
MILVUS_MAX_RESULTS=5                          # Maximum number of search results to return

# Embedding Model Configuration
EMBEDDING_MODEL="path/to/embedding/model/dir"
# You can also use a Hugging Face model name directly, e.g.:
# EMBEDDING_MODEL="sentence-transformers/distiluse-base-multilingual-cased-v2"
```


#### 3. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

#### 4. Integrate with Your IDE (MCP Server Setup)
The project functions as an [MCP (Model Control Protocol)](https://github.com/modelcontextprotocol/spec) server. To use it in your preferred IDE, configure the MCP client accordingly.

For example, in **Cline**, add the following entry to your `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "hl-mcp": {
      "command": "python3",
      "args": ["/path/to/hl-mcp/server.py"],
      "timeout": 3600,
      "env": {},
      "transportType": "stdio"
    }
  }
}
```

> Replace `/path/to/hl-mcp/server.py` with the actual absolute path to `server.py` in your cloned repository.

Once configured, the integration will appear in your IDE like this:

![Cline integration screenshot](https://github.com/user-attachments/assets/d148b8d4-d3be-48b4-9532-8176575a72b5)

---


### Embeding models

As you may have noticed, the directory `database/{version}/` contains several `.db` files. Each of these databases was generated using a different text embedding model. Below is a list of the supported models, ordered by increasing computational complexity and model size.

If you wish to use an embedding model not included in this list, you will need to generate a new vector database using embeddings produced by your chosen model.

| Database File                      | Model Name                                      | Model Card / Hugging Face Link                                                | Embedding Dimension | Max Sequence Length | Key Features |
|-----------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------|---------------------|----------------------|--------------|
| `hlr-distiluse-cv2-{version}.db`  | `distiluse-base-multilingual-cased-v2`           | [sentence-transformers/distiluse-base-multilingual-cased-v2](https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v2) | 512                 | 128                  | Lightweight, fast inference; suitable for basic multilingual semantic search |
| `hlr-e5-large-{version}.db`       | `multilingual-e5-large-instruct`                 | [intfloat/multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct) | 1024                | 512                  | Instruction-tuned; strong performance on retrieval tasks; supports 100 languages |
| `hlr-alibaba-gte-{version}.db`    | `gte-multilingual-base`                          | [Alibaba-NLP/gte-multilingual-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-base) | 768                 | 8192                 | Handles long contexts; supports dense and sparse embeddings; good cross-lingual retrieval |
| `hlr-baai-bge-m3-{version}.db`    | `BGE-M3`                                         | [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3)                              | 1024                | 8192                 | Multi-functional (dense, sparse, ColBERT); supports 100+ languages; state-of-the-art performance on multilingual benchmarks |

> **Note**: To incorporate a custom embedding model not listed above, you must re-embed your document collection and create a new vector database accordingly.

---

## Dataset Expansion

If you'd like to expand the dataset or use your own embedding model with Milvus, please use the prepared Colab notebook located in the Jupyter directory. It contains all the necessary code to add new data and integrate your custom embedding model.

