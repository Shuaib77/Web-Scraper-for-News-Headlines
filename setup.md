# Setup Instructions for News Headlines Web Scraper

## Quick Start Guide

### Prerequisites
- Python 3.6 or higher installed on your system
- Internet connection for web scraping
- Command line/terminal access
- Text editor (VS Code recommended)

### Installation Steps

1. **Check Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

2. **Download/Clone the Project**
   ```bash
   # If using git
   git clone <your-repo-url>
   cd news-headlines-scraper

   # Or download files manually and place them in a folder
   ```

3. **Install Required Packages**
   ```bash
   # Install dependencies
   pip install requests beautifulsoup4 lxml

   # Or install from requirements file
   pip install -r requirements.txt
   ```

4. **Project Files Structure**
   ```
   news-headlines-scraper/
   ├── news_scraper.py         # Main scraper application
   ├── requirements.txt        # Python dependencies
   ├── demo.py                # Demo script
   ├── test_scraper.py        # Test cases
   ├── README.md              # Documentation
   ├── setup.md               # This file
   ├── news_headlines.txt     # Generated headlines (after running)
   └── news_headlines.json    # Generated JSON data (after running)
   ```

### Running the Application

#### Method 1: Main Scraper (Interactive)
```bash
python news_scraper.py
```

#### Method 2: Demo Mode (No Internet Required)
```bash
python demo.py
```

#### Method 3: Run Tests
```bash
python test_scraper.py
```

### Package Installation Details

#### Required Packages
- **requests (>=2.31.0)**: For making HTTP requests to websites
- **beautifulsoup4 (>=4.12.0)**: For parsing HTML and extracting data
- **lxml (>=4.9.0)**: Fast XML and HTML parser (optional but recommended)

#### Installation Methods
```bash
# Method 1: Individual packages
pip install requests
pip install beautifulsoup4
pip install lxml

# Method 2: All at once
pip install requests beautifulsoup4 lxml

# Method 3: From requirements file
pip install -r requirements.txt
```

### Usage Guide

1. **Run the scraper**:
   ```bash
   python news_scraper.py
   ```

2. **Monitor output**:
   - Watch for connection messages
   - Check for successful scraping from each source
   - Note the number of headlines found

3. **Check generated files**:
   - `news_headlines.txt` - Text file with all headlines
   - `news_headlines.json` - Structured JSON data

4. **Review results**:
   - Open text file to read headlines
   - Use JSON file for data analysis

### Output Files Explained

#### news_headlines.txt
- Human-readable format
- Timestamped header
- Numbered headlines with source attribution
- Summary footer with total count

#### news_headlines.json
- Machine-readable structured data
- Contains metadata (timestamp, counts)
- Individual headline objects with ID, source, title
- Suitable for further data processing

### Troubleshooting

#### Common Issues and Solutions

**Problem**: "Module not found" error
```bash
# Solution: Install missing packages
pip install requests beautifulsoup4 lxml
```

**Problem**: "Connection refused" or timeout errors
```bash
# Solution: Check internet connection
ping google.com

# Or run demo mode instead
python demo.py
```

**Problem**: Permission denied for file creation
```bash
# Solution: Run from a directory with write permissions
cd ~/Documents
python news_scraper.py
```

**Problem**: "SSL Certificate" errors
```bash
# Solution: Update certificates or use requests with verify=False (not recommended for production)
pip install --upgrade certifi
```

**Problem**: No headlines extracted
```bash
# Solution: Websites may have changed structure
# Check demo.py for expected behavior
# Consider updating CSS selectors in news_scraper.py
```

#### Advanced Troubleshooting

**Debug Mode**: Add print statements to see what's happening
```python
# In news_scraper.py, add debug prints
print(f"Response status: {response.status_code}")
print(f"Content length: {len(response.content)}")
print(f"Found {len(soup.select('h2'))} h2 elements")
```

**Network Issues**: Test with simple requests
```python
import requests
response = requests.get('https://httpbin.org/get')
print(response.status_code)  # Should print 200
```

### Performance Optimization

#### For Better Results
- Run during off-peak hours for faster responses
- Ensure stable internet connection
- Close unnecessary applications to free up resources

#### Customization Options
- Modify `timeout` values in news_scraper.py for slower connections
- Adjust `time.sleep()` delays for more/less aggressive scraping
- Add more news sources by extending the scraper methods

### Security and Ethics

#### Best Practices
- Don't run the scraper too frequently (respect rate limits)
- Check websites' robots.txt files before scraping
- Use appropriate User-Agent headers (already implemented)
- Don't scrape private or authentication-required content

#### Legal Considerations
- Only scrapes publicly available headlines
- Educational use falls under fair use
- Respect website terms of service
- Don't republish content commercially without permission

### Development Environment

#### Recommended Setup
- **IDE**: VS Code with Python extension
- **Terminal**: Command Prompt (Windows) or Terminal (Mac/Linux)
- **Python**: Version 3.6 or higher
- **Internet**: Stable broadband connection

#### Testing Environment
- Run tests with: `python test_scraper.py`
- Run demo with: `python demo.py`
- Both work offline for development

### Next Steps

After successful setup and testing:
1. Run the main scraper: `python news_scraper.py`
2. Check the generated files
3. Customize for additional news sources if desired
4. Submit your GitHub repository as required
