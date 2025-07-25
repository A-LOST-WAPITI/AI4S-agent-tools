#!/usr/bin/env python3
"""
Generate a simple, Apple-style showcase page for AI4S Agent Tools.
"""
import json
from pathlib import Path
from datetime import datetime

def load_categories():
    """Load category definitions."""
    categories_path = Path(__file__).parent.parent / "config" / "categories.json"
    if categories_path.exists():
        with open(categories_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"categories": {}, "default_category": "research"}

def get_tool_category(tool: dict, categories_config: dict) -> str:
    """Get the category of a tool from its metadata."""
    # Use the category directly from the tool's metadata
    category = tool.get("category", "")
    
    # Validate that the category exists in our configuration
    if category in categories_config.get("categories", {}):
        return category
    
    # Fall back to default category if the tool's category is invalid or missing
    return categories_config.get("default_category", "general")

def generate_showcase():
    """Generate the showcase HTML page."""
    root_dir = Path(__file__).parent.parent
    tools_json_path = root_dir / "TOOLS.json"
    
    # Load tools data
    with open(tools_json_path, 'r', encoding='utf-8') as f:
        tools_data = json.load(f)
    
    # Load categories
    categories_config = load_categories()
    categories = categories_config["categories"]
    
    # Categorize tools using their metadata
    categorized_tools = {}
    for tool in tools_data["tools"]:
        category = get_tool_category(tool, categories_config)
        if category not in categorized_tools:
            categorized_tools[category] = []
        categorized_tools[category].append(tool)
    
    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI4S Agent Tools - Scientific Computing Tools for Intelligent Agents</title>
    <style>
        :root {{
            --primary: #3B82F6;
            --primary-dark: #1E40AF;
            --secondary: #8B5CF6;
            --accent: #06B6D4;
            --success: #10B981;
            --warning: #F59E0B;
            --danger: #EF4444;
            --dark: #0F172A;
            --dark-secondary: #1E293B;
            --light: #F8FAFC;
            --light-secondary: #F1F5F9;
            --gray: #64748B;
            --gray-light: #94A3B8;
            --bg: #FFFFFF;
            --card-bg: #FFFFFF;
            --border: #E2E8F0;
            --text: #334155;
            --text-light: #64748B;
        }}
        
        [data-theme="dark"] {{
            --bg: #0F172A;
            --card-bg: #1E293B;
            --border: #334155;
            --text: #F1F5F9;
            --text-light: #94A3B8;
            --light: #1E293B;
            --light-secondary: #334155;
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            transition: all 0.3s ease;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        .theme-toggle {{
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 50px;
            padding: 8px;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }}
        
        .theme-toggle:hover {{
            transform: scale(1.05);
        }}
        
        .hero {{
            background: linear-gradient(135deg, 
                rgba(59, 130, 246, 0.1) 0%, 
                rgba(139, 92, 246, 0.1) 25%,
                rgba(6, 182, 212, 0.1) 50%,
                rgba(16, 185, 129, 0.1) 100%);
            padding: 120px 0 80px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .hero::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 20% 50%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 40% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
            animation: pulse 4s ease-in-out infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; }}
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .mission {{
            animation: fadeInUp 1s ease-out 0.5s both;
        }}
        
        .hero-content {{
            position: relative;
            z-index: 1;
        }}
        
        h1 {{
            font-size: 4rem;
            font-weight: 700;
            margin-bottom: 1rem;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .subtitle {{
            font-size: 1.5rem;
            font-weight: 400;
            color: var(--text-light);
            margin-bottom: 2rem;
        }}
        
        .mission {{
            font-size: 1.35rem;
            font-weight: 300;
            max-width: 900px;
            margin: 0 auto 3rem;
            color: var(--text);
            line-height: 2;
            letter-spacing: 0.02em;
            text-align: center;
            position: relative;
        }}
        
        .mission::before {{
            content: '"';
            position: absolute;
            left: -30px;
            top: -10px;
            font-size: 4rem;
            opacity: 0.1;
            font-family: Georgia, serif;
        }}
        
        .mission-highlight {{
            color: var(--primary);
            font-weight: 400;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 3rem;
            margin-top: 3rem;
        }}
        
        .stat {{
            text-align: center;
            background: var(--card-bg);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }}
        
        .stat:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}
        
        .stat-value {{
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .stat-label {{
            font-size: 0.9rem;
            color: var(--text-light);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 0.5rem;
        }}
        
        .cta-buttons {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
        }}
        
        .btn {{
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }}
        
        .btn-primary {{
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
        }}
        
        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
        }}
        
        .btn-secondary {{
            border: 2px solid var(--border);
            color: var(--text);
        }}
        
        .btn-secondary:hover {{
            border-color: var(--primary);
            color: var(--primary);
        }}
        
        .search-container {{
            padding: 4rem 0;
            background: var(--light);
        }}
        
        .search-box {{
            position: relative;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        .search-input {{
            width: 100%;
            padding: 1rem 1.25rem 1rem 3.5rem;
            font-size: 1rem;
            border: 2px solid var(--border);
            border-radius: 50px;
            background: var(--card-bg);
            color: var(--text);
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }}
        
        .search-input:focus {{
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.2);
        }}
        
        .search-icon {{
            position: absolute;
            left: 1.25rem;
            top: 50%;
            transform: translateY(-50%);
            opacity: 0.5;
            font-size: 1.2rem;
        }}
        
        .categories {{
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 2rem;
        }}
        
        .category-tag {{
            padding: 0.5rem 1rem;
            border-radius: 50px;
            background: var(--card-bg);
            color: var(--text);
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid var(--border);
            font-weight: 500;
        }}
        
        .category-tag:hover {{
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
        }}
        
        .category-tag.active {{
            background: var(--primary);
            color: white;
            border-color: var(--primary);
        }}
        
        .quick-start {{
            padding: 4rem 0;
            background: var(--card-bg);
        }}
        
        .section-title {{
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 1rem;
            color: var(--text);
        }}
        
        .section-subtitle {{
            font-size: 1.2rem;
            text-align: center;
            color: var(--text-light);
            margin-bottom: 3rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .quick-start-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }}
        
        .quick-start-card {{
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
        }}
        
        .quick-start-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}
        
        .quick-start-card h3 {{
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--text);
        }}
        
        .code-snippet {{
            background: var(--dark);
            color: #E2E8F0;
            padding: 1.5rem;
            border-radius: 12px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 0.875rem;
            overflow-x: auto;
            margin: 1rem 0;
            line-height: 1.6;
            white-space: pre-wrap;
            word-break: break-word;
        }}
        
        .coming-soon {{
            padding: 4rem 0;
            background: var(--light);
        }}
        
        .coming-soon-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
        }}
        
        .coming-soon-item {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .coming-soon-item:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }}
        
        .coming-soon-icon {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}
        
        .coming-soon-title {{
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text);
        }}
        
        .tools-grid {{
            padding: 4rem 0;
        }}
        
        .category-section {{
            margin-bottom: 4rem;
        }}
        
        .category-header {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        
        .category-icon {{
            font-size: 2rem;
        }}
        
        .category-title {{
            font-size: 2rem;
            font-weight: 700;
            color: var(--text);
        }}
        
        .tools-row {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.5rem;
        }}
        
        .tool-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2rem;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }}
        
        .tool-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .tool-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}
        
        .tool-card:hover::before {{
            opacity: 1;
        }}
        
        .tool-header {{
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 1rem;
        }}
        
        .tool-name {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text);
        }}
        
        .tool-author {{
            font-size: 0.875rem;
            color: var(--text-light);
        }}
        
        .tool-description {{
            color: var(--text-light);
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }}
        
        .tool-features {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }}
        
        .tool-feature {{
            padding: 0.25rem 0.75rem;
            background: var(--light);
            border: 1px solid var(--border);
            border-radius: 20px;
            font-size: 0.75rem;
            color: var(--text);
            font-weight: 500;
        }}
        
        .tool-count {{
            font-size: 0.75rem;
            color: var(--text-light);
            margin-left: 0.5rem;
            font-style: italic;
        }}
        
        .community {{
            padding: 4rem 0;
            background: var(--card-bg);
            text-align: center;
        }}
        
        .community-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }}
        
        .community-item {{
            padding: 1.5rem;
        }}
        
        .community-icon {{
            font-size: 3rem;
            margin-bottom: 1rem;
        }}
        
        .community-title {{
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text);
        }}
        
        .community-desc {{
            color: var(--text-light);
            font-size: 0.9rem;
        }}
        
        footer {{
            padding: 3rem 0;
            text-align: center;
            background: var(--dark);
            color: #94A3B8;
        }}
        
        .footer-content {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }}
        
        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
        }}
        
        .footer-links a {{
            color: #94A3B8;
            text-decoration: none;
            transition: color 0.3s ease;
        }}
        
        .footer-links a:hover {{
            color: var(--primary);
        }}
        
        .modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.8);
            z-index: 1000;
            backdrop-filter: blur(8px);
        }}
        
        .modal-content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 3rem;
            max-width: 700px;
            width: 90%;
            max-height: 85vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
        }}
        
        .modal-close {{
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
            font-size: 1.5rem;
            color: var(--text-light);
            cursor: pointer;
            transition: color 0.3s ease;
        }}
        
        .modal-close:hover {{
            color: var(--text);
        }}
        
        .modal-title {{
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: var(--text);
        }}
        
        .modal-section {{
            margin-bottom: 2rem;
        }}
        
        .modal-section-title {{
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: var(--text);
        }}
        
        .code-block {{
            background: var(--dark);
            color: #E2E8F0;
            padding: 1.5rem;
            border-radius: 12px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 0.875rem;
            overflow-x: auto;
            line-height: 1.5;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2.5rem;
            }}
            
            .hero {{
                padding: 80px 0 60px;
            }}
            
            .stats {{
                gap: 1.5rem;
                flex-direction: column;
                align-items: center;
            }}
            
            .stat {{
                min-width: 200px;
            }}
            
            .stat-value {{
                font-size: 2.5rem;
            }}
            
            .tools-row {{
                grid-template-columns: 1fr;
            }}
            
            .quick-start-grid {{
                grid-template-columns: 1fr;
            }}
            
            .coming-soon-grid {{
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            }}
            
            .cta-buttons {{
                flex-direction: column;
                align-items: center;
            }}
            
            .modal-content {{
                padding: 2rem;
                margin: 1rem;
            }}
            
            .footer-links {{
                flex-direction: column;
                gap: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="theme-toggle" onclick="toggleTheme()">
        <span id="theme-icon">🌙</span>
    </div>
    
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>AI4S Agent Tools</h1>
                <p class="subtitle">Building intelligent tools for scientific research</p>
                <div class="mission">
                    We're building a comprehensive <span class="mission-highlight">scientific capability library</span><br>
                    Agent-ready tools that cover the full spectrum of AI for Science<br>
                    <em style="font-size: 1.1rem; opacity: 0.8;">An open project by the DeepModeling community</em>
                </div>
                <div class="cta-buttons">
                    <a href="https://github.com/deepmodeling/AI4S-agent-tools" class="btn btn-primary">🚀 Get Started</a>
                    <a href="https://github.com/deepmodeling/AI4S-agent-tools/blob/main/CONTRIBUTING.md" class="btn btn-secondary">🤝 Contribute</a>
                </div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value">{len(tools_data['tools'])}</div>
                        <div class="stat-label">Collections</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{sum(len(tool.get('tools', [])) for tool in tools_data['tools'])}</div>
                        <div class="stat-label">Tools</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">{len(set(tool.get('author', '@unknown') for tool in tools_data['tools']))}</div>
                        <div class="stat-label">Contributors</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section class="quick-start">
        <div class="container">
            <h2 class="section-title">Quick Start</h2>
            <p class="section-subtitle">Get up and running with AI4S tools in minutes</p>
            <div class="quick-start-grid">
                <div class="quick-start-card">
                    <h3>🔬 Use a Tool</h3>
                    <p>Install and run any scientific tool server</p>
                    <div class="code-snippet"># Navigate to tool directory
cd servers/&lt;toolname&gt;

# Install dependencies
uv sync

# Run the server
python server.py --port &lt;port&gt;</div>
                </div>
                <div class="quick-start-card">
                    <h3>🛠️ Add Your Tool</h3>
                    <p>Create your own scientific capability</p>
                    <div class="code-snippet"># Copy template
cp -r servers/_example servers/my_tool

# Edit and customize
cd servers/my_tool
# ... edit server.py ...

# Install and run
uv sync
python server.py --port &lt;port&gt;</div>
                </div>
            </div>
        </div>
    </section>
    
    <section class="coming-soon">
        <div class="container">
            <h2 class="section-title">Coming Soon</h2>
            <p class="section-subtitle">Exciting new capabilities in development</p>
            <div class="coming-soon-grid">
                <div class="coming-soon-item">
                    <div class="coming-soon-icon">📊</div>
                    <div class="coming-soon-title">Spectral Analysis</div>
                    <p>XRD, NMR, Raman analysis tools</p>
                </div>
                <div class="coming-soon-item">
                    <div class="coming-soon-icon">🧬</div>
                    <div class="coming-soon-title">Protein Structure</div>
                    <p>Prediction and analysis</p>
                </div>
                <div class="coming-soon-item">
                    <div class="coming-soon-icon">🔭</div>
                    <div class="coming-soon-title">3D Visualization</div>
                    <p>Molecular visualization tools</p>
                </div>
                <div class="coming-soon-item">
                    <div class="coming-soon-icon">📈</div>
                    <div class="coming-soon-title">Experimental Design</div>
                    <p>Optimization algorithms</p>
                </div>
                <div class="coming-soon-item">
                    <div class="coming-soon-icon">🧫</div>
                    <div class="coming-soon-title">Bayesian Optimization</div>
                    <p>Multi-objective optimization</p>
                </div>
            </div>
        </div>
    </section>
    
    <div class="search-container">
        <div class="container">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" class="search-input" placeholder="Search tools..." id="searchInput">
            </div>
            <div class="categories">
                <span class="category-tag active" data-category="all">All</span>
"""
    
    for cat_id, cat_info in categories.items():
        if cat_id in categorized_tools:
            html += f"""                <span class="category-tag" data-category="{cat_id}">{cat_info['icon']} {cat_info['name']}</span>
"""
    
    html += """            </div>
        </div>
    </div>
    
    <div class="tools-grid">
        <div class="container">
"""
    
    # Add tools by category
    for cat_id, tools in categorized_tools.items():
        if cat_id in categories:
            cat_info = categories[cat_id]
            html += f"""            <div class="category-section" data-category="{cat_id}">
                <div class="category-header">
                    <span class="category-icon">{cat_info['icon']}</span>
                    <h2 class="category-title">{cat_info['name']}</h2>
                </div>
                <div class="tools-row">
"""
            
            for tool in tools:
                features = tool.get('tools', [])[:3]
                more_count = len(tool.get('tools', [])) - 3
                
                html += f"""                    <div class="tool-card" onclick="showToolDetails('{tool['name']}')">
                        <div class="tool-header">
                            <div>
                                <div class="tool-name">{tool['name']}</div>
                                <div class="tool-author">{tool.get('author', '@unknown')}</div>
                            </div>
                        </div>
                        <p class="tool-description">{tool.get('description', 'No description available')}</p>
                        <div class="tool-features">
"""
                
                for feature in features:
                    html += f"""                            <span class="tool-feature">{feature}</span>
"""
                
                if more_count > 0:
                    html += f"""                            <span class="tool-count">+{more_count} more</span>
"""
                
                html += """                        </div>
                    </div>
"""
            
            html += """                </div>
            </div>
"""
    
    html += f"""        </div>
    </div>
    
    <section class="community">
        <div class="container">
            <h2 class="section-title">Join Our Community</h2>
            <p class="section-subtitle">We welcome contributions from scientists, developers, and AI researchers</p>
            <div class="community-grid">
                <div class="community-item">
                    <div class="community-icon">🧑‍🔬</div>
                    <div class="community-title">Domain Scientists</div>
                    <div class="community-desc">With computational needs</div>
                </div>
                <div class="community-item">
                    <div class="community-icon">💻</div>
                    <div class="community-title">Developers</div>
                    <div class="community-desc">Scientific computing enthusiasts</div>
                </div>
                <div class="community-item">
                    <div class="community-icon">🤖</div>
                    <div class="community-title">AI Researchers</div>
                    <div class="community-desc">Building science agents</div>
                </div>
                <div class="community-item">
                    <div class="community-icon">📚</div>
                    <div class="community-title">Open Science</div>
                    <div class="community-desc">Passionate about collaboration</div>
                </div>
            </div>
        </div>
    </section>
    
    <footer>
        <div class="footer-content">
            <div class="footer-links">
                <a href="https://github.com/deepmodeling/AI4S-agent-tools">GitHub</a>
                <a href="https://github.com/deepmodeling/AI4S-agent-tools/blob/main/CONTRIBUTING.md">Contributing</a>
                <a href="https://github.com/deepmodeling">DeepModeling</a>
                <a href="https://github.com/deepmodeling/AI4S-agent-tools/blob/main/LICENSE">License</a>
            </div>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d')} • Built with ❤️ by the <a href="https://github.com/deepmodeling" style="color: var(--primary);">DeepModeling</a> community</p>
        </div>
    </footer>
    
    <!-- Tool Details Modal -->
    <div id="toolModal" class="modal">
        <div class="modal-content">
            <span class="modal-close" onclick="closeModal()">&times;</span>
            <h2 class="modal-title" id="modalTitle"></h2>
            <div id="modalContent"></div>
        </div>
    </div>
    
    <script>
        const toolsData = {json.dumps(tools_data['tools'], indent=4)};
        
        // Theme toggle functionality
        function toggleTheme() {{
            const body = document.body;
            const themeIcon = document.getElementById('theme-icon');
            const currentTheme = body.getAttribute('data-theme');
            
            if (currentTheme === 'dark') {{
                body.removeAttribute('data-theme');
                themeIcon.textContent = '🌙';
                localStorage.setItem('theme', 'light');
            }} else {{
                body.setAttribute('data-theme', 'dark');
                themeIcon.textContent = '☀️';
                localStorage.setItem('theme', 'dark');
            }}
        }}
        
        // Initialize theme from localStorage
        document.addEventListener('DOMContentLoaded', function() {{
            const savedTheme = localStorage.getItem('theme');
            const themeIcon = document.getElementById('theme-icon');
            
            if (savedTheme === 'dark') {{
                document.body.setAttribute('data-theme', 'dark');
                themeIcon.textContent = '☀️';
            }} else {{
                themeIcon.textContent = '🌙';
            }}
        }});
        
        // Search functionality
        document.getElementById('searchInput').addEventListener('input', function(e) {{
            const searchTerm = e.target.value.toLowerCase();
            filterTools(searchTerm);
        }});
        
        // Category filter
        document.querySelectorAll('.category-tag').forEach(tag => {{
            tag.addEventListener('click', function() {{
                document.querySelectorAll('.category-tag').forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                
                const category = this.dataset.category;
                if (category === 'all') {{
                    document.querySelectorAll('.category-section').forEach(section => {{
                        section.style.display = 'block';
                    }});
                }} else {{
                    document.querySelectorAll('.category-section').forEach(section => {{
                        section.style.display = section.dataset.category === category ? 'block' : 'none';
                    }});
                }}
            }});
        }});
        
        function filterTools(searchTerm) {{
            document.querySelectorAll('.tool-card').forEach(card => {{
                const text = card.textContent.toLowerCase();
                card.style.display = text.includes(searchTerm) ? 'block' : 'none';
            }});
        }}
        
        function showToolDetails(toolName) {{
            const tool = toolsData.find(t => t.name === toolName);
            if (!tool) return;
            
            document.getElementById('modalTitle').textContent = tool.name;
            
            let content = `
                <div class="modal-section">
                    <div class="modal-section-title">Description</div>
                    <p>${{tool.description || 'No description available'}}</p>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">Author</div>
                    <p>${{tool.author || '@unknown'}}</p>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">Installation</div>
                    <div class="code-block">${{tool.install_command || `cd ${{tool.path}} && uv sync`}}</div>
                </div>
                
                <div class="modal-section">
                    <div class="modal-section-title">Start Command</div>
                    <div class="code-block">${{tool.start_command}}</div>
                </div>
            `;
            
            if (tool.tools && tool.tools.length > 0) {{
                content += `
                    <div class="modal-section">
                        <div class="modal-section-title">Available Functions (${{tool.tools.length}})</div>
                        <div class="tool-features">
                `;
                tool.tools.forEach(t => {{
                    content += `<span class="tool-feature">${{t}}</span>`;
                }});
                content += `
                        </div>
                    </div>
                `;
            }}
            
            document.getElementById('modalContent').innerHTML = content;
            document.getElementById('toolModal').style.display = 'block';
        }}
        
        function closeModal() {{
            document.getElementById('toolModal').style.display = 'none';
        }}
        
        // Close modal when clicking outside
        window.onclick = function(event) {{
            const modal = document.getElementById('toolModal');
            if (event.target == modal) {{
                modal.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>"""
    
    # Write HTML file
    showcase_dir = root_dir / "showcase"
    showcase_dir.mkdir(exist_ok=True)
    
    with open(showcase_dir / "index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Generated showcase page at: {showcase_dir / 'index.html'}")
    print(f"📊 Stats: {len(tools_data['tools'])} tools in {len(categorized_tools)} categories")

if __name__ == "__main__":
    generate_showcase()