from flask import Flask, jsonify, request
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connection

# Graph data structure
GRAPH = {
    'nodes': [
        {'id': 'Warehouse', 'x': 150, 'y': 100},
        {'id': 'A', 'x': 350, 'y': 80},
        {'id': 'B', 'x': 550, 'y': 100},
        {'id': 'C', 'x': 150, 'y': 250},
        {'id': 'D', 'x': 350, 'y': 220},
        {'id': 'E', 'x': 550, 'y': 250},
        {'id': 'F', 'x': 750, 'y': 200},
        {'id': 'G', 'x': 250, 'y': 400},
        {'id': 'H', 'x': 450, 'y': 380},
        {'id': 'I', 'x': 650, 'y': 400},
        {'id': 'J', 'x': 450, 'y': 520}
    ],
    'edges': [
        {'from': 'Warehouse', 'to': 'A', 'weight': 5},
        {'from': 'Warehouse', 'to': 'C', 'weight': 8},
        {'from': 'A', 'to': 'B', 'weight': 7},
        {'from': 'A', 'to': 'D', 'weight': 6},
        {'from': 'B', 'to': 'E', 'weight': 4},
        {'from': 'B', 'to': 'F', 'weight': 9},
        {'from': 'C', 'to': 'D', 'weight': 3},
        {'from': 'C', 'to': 'G', 'weight': 10},
        {'from': 'D', 'to': 'E', 'weight': 5},
        {'from': 'D', 'to': 'H', 'weight': 7},
        {'from': 'E', 'to': 'F', 'weight': 6},
        {'from': 'E', 'to': 'I', 'weight': 8},
        {'from': 'F', 'to': 'I', 'weight': 5},
        {'from': 'G', 'to': 'H', 'weight': 4},
        {'from': 'G', 'to': 'J', 'weight': 12},
        {'from': 'H', 'to': 'I', 'weight': 6},
        {'from': 'H', 'to': 'J', 'weight': 5},
        {'from': 'I', 'to': 'J', 'weight': 7},
        {'from': 'D', 'to': 'A', 'weight': 6},
        {'from': 'E', 'to': 'D', 'weight': 5},
        {'from': 'I', 'to': 'E', 'weight': 8},
        {'from': 'J', 'to': 'H', 'weight': 5},
        {'from': 'A', 'to': 'Warehouse', 'weight': 5},
        {'from': 'B', 'to': 'A', 'weight': 7},
        {'from': 'C', 'to': 'Warehouse', 'weight': 8}
    ]
}


class FloydWarshall:
    """
    Implementation of the Floyd-Warshall algorithm for finding
    all-pairs shortest paths in a weighted directed graph.
    """
    
    def __init__(self, graph):
        self.nodes = graph['nodes']
        self.edges = graph['edges']
        self.n = len(self.nodes)
        self.node_index = {node['id']: i for i, node in enumerate(self.nodes)}
        
        # Initialize distance and next matrices
        self.dist = [[float('inf')] * self.n for _ in range(self.n)]
        self.next = [[None] * self.n for _ in range(self.n)]
        
        # Set diagonal to 0 (distance from node to itself)
        for i in range(self.n):
            self.dist[i][i] = 0
        
        # Add edges to distance matrix
        for edge in self.edges:
            u = self.node_index[edge['from']]
            v = self.node_index[edge['to']]
            self.dist[u][v] = edge['weight']
            self.next[u][v] = v
        
        # Run the algorithm
        self.compute()
    
    def compute(self):
        """
        Execute the Floyd-Warshall algorithm.
        Time Complexity: O(V³) where V is the number of vertices.
        """
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dist[i][k] + self.dist[k][j] < self.dist[i][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next[i][j] = self.next[i][k]
    
    def get_path(self, start, end):
        """
        Reconstruct the shortest path from start to end.
        Returns a list of node IDs representing the path.
        """
        u = self.node_index.get(start)
        v = self.node_index.get(end)
        
        if u is None or v is None:
            return None
        
        if self.next[u][v] is None:
            return None  # No path exists
        
        path = [u]
        current = u
        
        while current != v:
            current = self.next[current][v]
            path.append(current)
        
        # Convert indices back to node IDs
        return [self.nodes[i]['id'] for i in path]
    
    def get_distance(self, start, end):
        """
        Get the shortest distance from start to end.
        """
        u = self.node_index.get(start)
        v = self.node_index.get(end)
        
        if u is None or v is None:
            return float('inf')
        
        return self.dist[u][v]


# Initialize Floyd-Warshall algorithm on server start
print("🚀 Initializing Floyd-Warshall algorithm...")
floyd_warshall = FloydWarshall(GRAPH)
print("✅ Algorithm initialized successfully!")


@app.route('/')
def index():
    """Home endpoint"""
    return jsonify({
        'message': 'Optimal Route Planner API',
        'version': '1.0.0',
        'endpoints': {
            '/api/graph': 'GET - Get graph structure',
            '/api/shortest-path': 'POST - Calculate shortest path'
        }
    })


@app.route('/api/graph', methods=['GET'])
def get_graph():
    """Return the graph structure"""
    return jsonify(GRAPH)


@app.route('/api/shortest-path', methods=['POST'])
def calculate_shortest_path():
    """
    Calculate the shortest path between two nodes.
    
    Expected JSON body:
    {
        "start": "A",
        "end": "B"
    }
    
    Returns:
    {
        "path": ["A", "D", "E", "B"],
        "distance": 15,
        "success": true
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'start' not in data or 'end' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing start or end parameters'
            }), 400
        
        start = data['start']
        end = data['end']
        
        # Validate nodes exist
        node_ids = [node['id'] for node in GRAPH['nodes']]
        if start not in node_ids or end not in node_ids:
            return jsonify({
                'success': False,
                'error': 'Invalid start or end node'
            }), 400
        
        # Get path and distance
        path = floyd_warshall.get_path(start, end)
        distance = floyd_warshall.get_distance(start, end)
        
        if path is None or distance == float('inf'):
            return jsonify({
                'success': False,
                'path': None,
                'distance': None,
                'message': f'No path exists between {start} and {end}'
            })
        
        return jsonify({
            'success': True,
            'path': path,
            'distance': distance,
            'stops': len(path) - 1
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/all-paths', methods=['GET'])
def get_all_paths():
    """
    Get all shortest paths between all pairs of nodes.
    Useful for debugging and analysis.
    """
    all_paths = {}
    
    for i, node_i in enumerate(GRAPH['nodes']):
        all_paths[node_i['id']] = {}
        for j, node_j in enumerate(GRAPH['nodes']):
            if i != j:
                path = floyd_warshall.get_path(node_i['id'], node_j['id'])
                distance = floyd_warshall.get_distance(node_i['id'], node_j['id'])
                
                all_paths[node_i['id']][node_j['id']] = {
                    'path': path,
                    'distance': distance if distance != float('inf') else None
                }
    
    return jsonify(all_paths)


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'algorithm': 'Floyd-Warshall',
        'nodes': len(GRAPH['nodes']),
        'edges': len(GRAPH['edges'])
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🗺️  OPTIMAL ROUTE PLANNER - BACKEND SERVER")
    print("="*60)
    print(f"📊 Graph loaded: {len(GRAPH['nodes'])} nodes, {len(GRAPH['edges'])} edges")
    print("🌐 Server starting on http://localhost:5000")
    print("📡 CORS enabled for frontend communication")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
