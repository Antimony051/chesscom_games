# **♟ Chess.com Game history downloader**  

This project downloads chess game archives from [Chess.com](https://www.chess.com), extracts game data from HTML tables, and compiles them into a structured CSV file.  

## **📌 Features**  
✅ Downloads recent chess games from Chess.com  
✅ Extracts game data from HTML files  
✅ Compiles all games into a single CSV file  

---

## **🛠 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/chess-scraper.git
cd chess-scraper
```

### **2️⃣ Install Dependencies**  
Ensure you have Python 3.x installed, then install required packages:  
```sh
pip install pandas requests
```

### **3️⃣ Update Configuration**  
Modify the following **before running**:  
- **Set the output directory** in `main()` (both scripts).  
- **Replace `"<your_cookie_here>"`** in `HEADERS` if authentication is required.  

---

## **🚀 Usage**  

### **1️⃣ Download Chess Games**  
Run the script to fetch and save game pages:  
```sh
python download_html_files.py
```
✔ Downloads missing pages into `path/to/your/games/folder`  
✔ Handles rate limits by waiting when needed  

---

### **2️⃣ Extract Tables & Compile CSV**  
After downloading, process the data with:  
```sh
python process_html_files.py
```
✔ Parses tables from saved HTML files  
✔ Combines all data into `combined_tables.csv`  

---

## **📄 CSV Output Format**  

The final **CSV file (`combined_tables.csv`)** has the following **columns**:  

| Time Control | Players | Result | Accuracy | Moves | Date |
|--------------|---------|--------|----------|-------|------|
| 3|2          | PlayerA (1500) vs PlayerB (1400) | 1-0 | 85% | 35 | Feb 15, 2025 |
| 5|0          | PlayerX (1600) vs PlayerY (1550) | 0-1 | Review | 42 | Feb 14, 2025 |

---

## **🔧 Customization**  
- **Change the number of pages downloaded** in `find_missing_pages()` (default: `101`).  
- **Modify file storage paths** in `OUTPUT_DIRECTORY`.  

---

## **📌 Notes**  
⚠️ **Respect Chess.com’s rate limits** to avoid getting blocked.  
⚠️ If authentication is needed, **update the `Cookie` header**.  

---

## **📜 License**  
This project is licensed under the **MIT License**.  
