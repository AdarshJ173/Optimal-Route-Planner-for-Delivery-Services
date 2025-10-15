# 🗺️ Optimal Route Planner

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**An interactive visualization of the Floyd-Warshall algorithm for finding optimal delivery routes**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-documentation) • [Algorithm](#-algorithm-explanation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Algorithm Explanation](#-algorithm-explanation)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Optimal Route Planner** is a full-stack web application that demonstrates the Floyd-Warshall algorithm in action. It helps visualize how shortest paths are computed in a weighted directed graph, making it perfect for understanding route optimization in delivery services, logistics, and network planning.

The application features a **Python Flask backend** that implements the Floyd-Warshall algorithm and a **responsive HTML/CSS/JavaScript frontend** that provides an interactive visualization of the graph and computed paths.

---

## ✨ Features

### 🚀 Core Features

- **Floyd-Warshall Algorithm Implementation** - Efficient all-pairs shortest path computation in O(V³) time
- **Interactive Graph Visualization** - Canvas-based rendering with real-time path highlighting
- **Python Backend API** - RESTful Flask server with CORS support
- **Real-time Path Calculation** - Instant route computation via API calls
- **Responsive Design** - Modern, mobile-friendly interface
- **Directed Graph Support** - Handles one-way routes and asymmetric weights

### 🎨 Visualization Features

- Color-coded nodes (start, end, intermediate)
- Animated path highlighting
- Directional arrows showing route flow
- Edge weights displayed on paths
- Visual legend for easy interpretation

### 🔧 Technical Features

- RESTful API with multiple endpoints
- CORS-enabled for cross-origin requests
- Error handling and validation
- Health check endpoint
- Comprehensive API documentation

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask 3.0.0** - Web framework
- **Flask-CORS 4.0.0** - Cross-Origin Resource Sharing

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with flexbox/grid
- **Vanilla JavaScript (ES6+)** - No frameworks required
- **Canvas API** - Graph visualization

### Algorithm
- **Floyd-Warshall** - All-pairs shortest path algorithm

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/optimal-route-planner.git
   cd optimal-route-planner
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python --version  # Should be 3.8+
   pip list          # Should show Flask and flask-cors
   ```

---

## 🚀 Usage

### Starting the Backend Server

1. **Run the Flask server**
   ```bash
   python app.py
   ```

2. **Verify the server is running**
   - You should see output like:
   ```
   ============================================================
   🗺️  OPTIMAL ROUTE PLANNER - BACKEND SERVER
   ============================================================
   📊 Graph loaded: 11 nodes, 25 edges
   🌐 Server starting on http://localhost:5000
   📡 CORS enabled for frontend communication
   ============================================================
   ```

3. **Test the API** (optional)
   ```bash
   curl http://localhost:5000/health
   ```

### Opening the Frontend

1. **Open `index.html` in your browser**
   - Double-click `index.html`, or
   - Right-click → Open with → Your browser, or
   - Use a local server:
     ```bash
     # Python 3
     python -m http.server 8000
     # Then visit http://localhost:8000
     ```

2. **Use the application**
   - Select a **Start Location** from the dropdown
   - Select an **End Location** from the dropdown
   - Click **Find Optimal Route**
   - View the highlighted path and travel time!

---

## 📁 Project Structure

```
optimal-route-planner/
│
├── app.py                 # Flask backend server with Floyd-Warshall implementation
├── index.html             # Frontend HTML with embedded CSS and JavaScript
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
└── .git/                 # Git repository (if initialized)
```

---

## 🌐 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. **Get API Information**
```http
GET /
```

**Response:**
```json
{
  "message": "Optimal Route Planner API",
  "version": "1.0.0",
  "endpoints": {
    "/api/graph": "GET - Get graph structure",
    "/api/shortest-path": "POST - Calculate shortest path"
  }
}
```

---

#### 2. **Get Graph Structure**
```http
GET /api/graph
```

**Response:**
```json
{
  "nodes": [
    {"id": "Warehouse", "x": 150, "y": 100},
    {"id": "A", "x": 350, "y": 80},
    ...
  ],
  "edges": [
    {"from": "Warehouse", "to": "A", "weight": 5},
    {"from": "A", "to": "B", "weight": 7},
    ...
  ]
}
```

---

#### 3. **Calculate Shortest Path**
```http
POST /api/shortest-path
Content-Type: application/json
```

**Request Body:**
```json
{
  "start": "Warehouse",
  "end": "J"
}
```

**Response (Success):**
```json
{
  "success": true,
  "path": ["Warehouse", "C", "D", "H", "J"],
  "distance": 23,
  "stops": 4
}
```

**Response (No Path):**
```json
{
  "success": false,
  "path": null,
  "distance": null,
  "message": "No path exists between A and B"
}
```

---

#### 4. **Get All Paths**
```http
GET /api/all-paths
```

Returns shortest paths between all pairs of nodes.

---

#### 5. **Health Check**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "algorithm": "Floyd-Warshall",
  "nodes": 11,
  "edges": 25
}
```

---

## 🧮 Algorithm Explanation

### Floyd-Warshall Algorithm

The **Floyd-Warshall algorithm** is a dynamic programming algorithm for finding shortest paths between all pairs of vertices in a weighted directed graph.

#### Time Complexity: O(V³)
#### Space Complexity: O(V²)

### How It Works

1. **Initialize Distance Matrix**
   - Set `dist[i][i] = 0` for all nodes
   - Set `dist[u][v] = weight` for each edge (u, v)
   - Set `dist[i][j] = ∞` for all other pairs

2. **Initialize Next Matrix**
   - Set `next[u][v] = v` for each edge (u, v)
   - Used to reconstruct the actual path

3. **Dynamic Programming**
   ```python
   for k in range(n):
       for i in range(n):
           for j in range(n):
               if dist[i][k] + dist[k][j] < dist[i][j]:
                   dist[i][j] = dist[i][k] + dist[k][j]
                   next[i][j] = next[i][k]
   ```

4. **Path Reconstruction**
   - Follow the `next` pointers from start to end
   - Builds the actual sequence of nodes in the optimal path

### Why Floyd-Warshall?

- ✅ Computes **all-pairs** shortest paths (useful for route planning)
- ✅ Works with **negative edge weights** (unlike Dijkstra)
- ✅ Simple to implement and understand
- ✅ Pre-computation enables O(1) path queries

---

## 📸 Screenshots

### Main Interface
*[Add screenshot of your application here]*

### Path Visualization
*[Add screenshot of highlighted path here]*

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more graph layouts
- Implement other shortest path algorithms (Dijkstra, Bellman-Ford)
- Add graph editing functionality
- Improve mobile responsiveness
- Add unit tests
- Create Docker containerization

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Algorithm implementation based on the Floyd-Warshall algorithm
- Visualization inspired by graph theory educational tools
- Built with modern web technologies

---

## 📧 Contact

**Project Maintainer:** Your Name

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repository if you find it helpful!

</div>
