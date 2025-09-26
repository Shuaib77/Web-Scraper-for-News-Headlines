# Create demo script for the web scraper
demo_code = '''#!/usr/bin/env python3
"""
Demo script for News Headlines Web Scraper
This script demonstrates web scraping concepts without making actual requests
"""

import time
from datetime import datetime
import json

def demo_http_requests():
    """Demonstrate HTTP request concepts"""
    print("🌐 HTTP Requests Demo")
    print("=" * 40)
    
    # Mock HTTP request data
    demo_request = {
        "method": "GET",
        "url": "https://www.bbc.com/news",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"
        },
        "timeout": 10
    }
    
    print("📡 Sample HTTP GET Request:")
    print(f"   URL: {demo_request['url']}")
    print(f"   Method: {demo_request['method']}")
    print(f"   Timeout: {demo_request['timeout']} seconds")
    print("   Headers:")
    for key, value in demo_request['headers'].items():
        print(f"     {key}: {value[:50]}...")
    
    # Mock response
    demo_response = {
        "status_code": 200,
        "reason": "OK",
        "content_length": 150000,
        "content_type": "text/html; charset=utf-8"
    }
    
    print("\\n📥 Sample HTTP Response:")
    print(f"   Status Code: {demo_response['status_code']} ({demo_response['reason']})")
    print(f"   Content-Type: {demo_response['content_type']}")
    print(f"   Content-Length: {demo_response['content_length']:,} bytes")
    
    return demo_response

def demo_html_parsing():
    """Demonstrate HTML parsing concepts"""
    print("\\n🏷️ HTML Parsing Demo")
    print("=" * 40)
    
    # Sample HTML content
    sample_html = '''
    <html>
        <head><title>BBC News</title></head>
        <body>
            <h1 class="main-headline">Breaking: Major Story</h1>
            <h2 data-testid="card-headline">Technology Update</h2>
            <h2 class="story-title">Economic News</h2>
            <h3 id="sports-headline">Sports Results</h3>
            <div class="content">
                <p>News content here...</p>
            </div>
        </body>
    </html>
    '''
    
    print("📄 Sample HTML Structure:")
    print(sample_html.strip())
    
    # Demonstrate parsing concepts
    print("\\n🎯 CSS Selectors Used:")
    selectors = [
        'h1.main-headline',
        'h2[data-testid="card-headline"]',
        'h2.story-title',
        'h3#sports-headline',
        'h1, h2, h3'  # Multiple selector
    ]
    
    for selector in selectors:
        print(f"   {selector}")
    
    # Mock extracted headlines
    extracted_headlines = [
        "Breaking: Major Story",
        "Technology Update", 
        "Economic News",
        "Sports Results"
    ]
    
    print("\\n📰 Extracted Headlines:")
    for i, headline in enumerate(extracted_headlines, 1):
        print(f"   {i}. {headline}")
    
    return extracted_headlines

def demo_data_processing():
    """Demonstrate data processing and file operations"""
    print("\\n💾 Data Processing Demo")
    print("=" * 40)
    
    # Sample scraped data
    raw_headlines = [
        "[BBC] Global climate summit reaches agreement",
        "[CNN] Tech stocks surge in morning trading",
        "[Reuters] Central bank policy announcement",
        "[BBC] Sports championship results announced",
        "[CNN] Breaking: Market volatility continues",
        "[CNN] Tech stocks surge in morning trading",  # Duplicate
        "[Reuters] Economic indicators show growth"
    ]
    
    print("📊 Raw Headlines Collected:")
    for i, headline in enumerate(raw_headlines, 1):
        print(f"   {i}. {headline}")
    
    # Demonstrate duplicate removal
    seen = set()
    unique_headlines = []
    
    for headline in raw_headlines:
        headline_text = headline.split("] ", 1)[1] if "] " in headline else headline
        if headline_text not in seen:
            seen.add(headline_text)
            unique_headlines.append(headline)
    
    print(f"\\n🔄 After Duplicate Removal:")
    print(f"   Original: {len(raw_headlines)} headlines")
    print(f"   Unique: {len(unique_headlines)} headlines")
    print(f"   Duplicates removed: {len(raw_headlines) - len(unique_headlines)}")
    
    return unique_headlines

def demo_file_operations(headlines):
    """Demonstrate file save operations"""
    print("\\n📁 File Operations Demo")
    print("=" * 40)
    
    # Demo text file format
    print("📝 Text File Format (news_headlines.txt):")
    print("-" * 50)
    print(f"NEWS HEADLINES SCRAPED ON {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    for i, headline in enumerate(headlines[:5], 1):
        print(f"{i:3d}. {headline}")
    
    print(f"    ... and {len(headlines) - 5} more headlines")
    print("=" * 50)
    print(f"Total Headlines: {len(headlines)}")
    
    # Demo JSON format
    print("\\n📊 JSON File Format (news_headlines.json):")
    print("-" * 50)
    
    json_data = {
        "scrape_timestamp": datetime.now().isoformat(),
        "total_headlines": len(headlines),
        "headlines": [
            {
                "id": i,
                "source": headline.split("] ")[0].replace("[", ""),
                "title": headline.split("] ", 1)[1] if "] " in headline else headline,
                "full_text": headline
            }
            for i, headline in enumerate(headlines[:3], 1)
        ]
    }
    
    print(json.dumps(json_data, indent=2)[:300] + "...")

def demo_error_handling():
    """Demonstrate error handling scenarios"""
    print("\\n🛡️ Error Handling Demo")
    print("=" * 40)
    
    # Common error scenarios
    error_scenarios = [
        {
            "error": "requests.ConnectionError",
            "cause": "No internet connection",
            "handling": "Skip source and continue with other sites"
        },
        {
            "error": "requests.HTTPError", 
            "cause": "404 Not Found or 403 Forbidden",
            "handling": "Log error and try alternative URLs"
        },
        {
            "error": "requests.Timeout",
            "cause": "Server response too slow",
            "handling": "Retry with longer timeout or skip"
        },
        {
            "error": "BeautifulSoup parsing error",
            "cause": "Malformed HTML content",
            "handling": "Use alternative parsers or selectors"
        },
        {
            "error": "FileNotFoundError",
            "cause": "Cannot create output file",
            "handling": "Check permissions and disk space"
        }
    ]
    
    print("🚨 Common Error Scenarios:")
    for i, scenario in enumerate(error_scenarios, 1):
        print(f"\\n{i}. {scenario['error']}")
        print(f"   Cause: {scenario['cause']}")
        print(f"   Handling: {scenario['handling']}")

def demo_web_scraping_ethics():
    """Demonstrate web scraping best practices"""
    print("\\n⚖️ Web Scraping Ethics Demo")
    print("=" * 40)
    
    best_practices = [
        {
            "practice": "Rate Limiting",
            "description": "Add delays between requests",
            "implementation": "time.sleep(1) between requests"
        },
        {
            "practice": "User-Agent Headers",
            "description": "Identify your scraper properly",
            "implementation": "Mozilla/5.0 browser identification"
        },
        {
            "practice": "Respect robots.txt",
            "description": "Check site scraping permissions",
            "implementation": "Read /robots.txt before scraping"
        },
        {
            "practice": "Handle HTTP Status Codes",
            "description": "Respect server responses",
            "implementation": "Stop on 403, retry on 500"
        },
        {
            "practice": "Public Data Only",
            "description": "Don't bypass authentication",
            "implementation": "Only scrape publicly visible content"
        }
    ]
    
    print("✅ Best Practices Implemented:")
    for practice in best_practices:
        print(f"\\n• {practice['practice']}")
        print(f"  Description: {practice['description']}")
        print(f"  Implementation: {practice['implementation']}")

def run_complete_demo():
    """Run the complete web scraper demo"""
    print("🚀 News Headlines Web Scraper - Demo Mode")
    print("=" * 60)
    print("This demo shows web scraping concepts without making actual requests\\n")
    
    # Run all demo sections
    demo_http_requests()
    extracted_headlines = demo_html_parsing()
    unique_headlines = demo_data_processing()
    demo_file_operations(unique_headlines)
    demo_error_handling()
    demo_web_scraping_ethics()
    
    print("\\n" + "=" * 60)
    print("🎯 Demo Summary:")
    print("  ✅ HTTP requests and headers explained")
    print("  ✅ HTML parsing with CSS selectors shown")
    print("  ✅ Data processing and duplicate removal")
    print("  ✅ File operations (TXT and JSON) demonstrated")
    print("  ✅ Error handling scenarios covered")
    print("  ✅ Web scraping ethics and best practices")
    print("=" * 60)
    
    print("\\n🏃‍♂️ To run the actual scraper:")
    print("   1. Install requirements: pip install -r requirements.txt")
    print("   2. Run scraper: python news_scraper.py")
    print("   3. Check output files: news_headlines.txt")

if __name__ == "__main__":
    run_complete_demo()
'''

with open('demo.py', 'w', encoding='utf-8') as f:
    f.write(demo_code)

print("✅ demo.py created successfully!")

# Run the demo to show it works
print("\\n🧪 Running demo to show functionality...")
exec(demo_code)
