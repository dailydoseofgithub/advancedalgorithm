import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Main application

class EmergencyNetworkSimulator:

    def __init__(self, root):
        self.root = root
        self.root.title("Project: Emergency Network Simulator")
        self.root.geometry("1100x650")
       

        try:
            self.root.iconbitmap("network.ico")
        except:
            pass


        self.graph = nx.Graph()
        self.failed_nodes = set()

        self.setup_layout()
        self.draw_graph()

    # Layout

    def setup_layout(self):
        self.control = tk.Frame(self.root, bg="#2c3e50", width=260)
        self.control.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.control, text="Emergency Simulator",
                 bg="#2c3e50", fg="white",
                 font=("Arial", 16, "bold")).pack(pady=15)

        self.section("Network Setup")
        self.btn("Add City", self.add_node)
        self.btn("Add Road", self.add_edge)

        self.section("Algorithms")
        self.btn("Minimum Spanning Tree", self.show_mst)
        self.btn("Reliable Path Finder", self.reliable_paths)

        self.section("Simulation")
        self.btn("Simulate Node Failure", self.simulate_failure)

        self.section("Extras")
        self.btn("Graph Coloring", self.graph_coloring)
        self.btn("Command Hierarchy Optimizer", self.command_tree)

        self.status = tk.Label(self.control, text="Ready",
                               bg="#34495e", fg="white",
                               anchor="w")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        self.graph_frame = tk.Frame(self.root, bg="white")
        self.graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig, self.ax = plt.subplots(figsize=(7, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    # UI/UX part

    def btn(self, text, cmd):
        tk.Button(self.control, text=text, command=cmd,
                  bg="#ecf0f1", fg="#2c3e50",
                  relief="flat",
                  font=("Arial", 11),
                  padx=10, pady=6).pack(fill=tk.X, padx=20, pady=4)

    def section(self, title):
        tk.Label(self.control, text=title,
                 bg="#2c3e50", fg="#f1c40f",
                 font=("Arial", 12, "bold")).pack(pady=(15, 5))


    # Drawing graph

    def draw_graph(self, highlight_edges=None, title="Emergency Network"):
        self.ax.clear()
        pos = nx.spring_layout(self.graph, seed=42)

        nx.draw(self.graph, pos,
                ax=self.ax,
                with_labels=True,
                node_size=700,
                node_color="#74b9ff",
                edge_color="#636e72",
                font_size=10)

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        if highlight_edges and isinstance(highlight_edges, (list, tuple)):
            nx.draw_networkx_edges(
                self.graph, pos,
                edgelist=highlight_edges,
                width=3,
                edge_color="#27ae60",
                ax=self.ax
            )

        self.ax.set_title(title, fontsize=14, fontweight="bold")
        self.canvas.draw()


    # Adding node

    def add_node(self):
        node = simpledialog.askstring("Add City", "City name:")
        if node:
            self.graph.add_node(node)
            self.status.config(text=f"Added city: {node}")
            self.draw_graph()


    # Adding edge

    def add_edge(self):
        u = simpledialog.askstring("Add Road", "From city:")
        v = simpledialog.askstring("Add Road", "To city:")
        w = simpledialog.askinteger("Weight", "Distance / Time:")

        if u and v and w:
            self.graph.add_edge(u, v, weight=w)
            self.status.config(text=f"Road added: {u} ↔ {v}")
            self.draw_graph()


    # MST

    def show_mst(self):
        if len(self.graph.nodes) == 0:
            return

        mst = nx.minimum_spanning_tree(self.graph)
        total_weight = sum(self.graph[u][v]['weight'] for u, v in mst.edges())

        self.ax.clear()
        pos = nx.spring_layout(self.graph, seed=42)

        nx.draw(self.graph, pos,
                ax=self.ax,
                with_labels=True,
                node_size=700,
                node_color="#74b9ff",
                edge_color="#b2bec3")

        nx.draw_networkx_edges(
            self.graph, pos,
            edgelist=mst.edges(),
            width=3,
            edge_color="#27ae60",
            ax=self.ax
        )

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

       
        self.ax.text(
            0.02, 0.95,
            f"Total MST Weight = {total_weight}",
            transform=self.ax.transAxes,
            fontsize=13,
            fontweight="bold",
            verticalalignment="top"
        )

        self.ax.set_title("Minimum Spanning Tree", fontsize=15, fontweight="bold")
        self.status.config(text=f"MST generated | Total Weight = {total_weight}")
        self.canvas.draw()


    # Reliable path

    def reliable_paths(self):
        src = simpledialog.askstring("Source", "Source city:")
        dst = simpledialog.askstring("Destination", "Destination city:")

        try:
            path = nx.shortest_path(self.graph, src, dst, weight='weight')
            edges = list(zip(path, path[1:]))
            self.status.config(text=f"Reliable path: {src} → {dst}")
            self.draw_graph(edges, "Reliable Communication Path")
        except:
            messagebox.showinfo("No Path", "Path not available")


    # Failure simulation

    def simulate_failure(self):
        node = simpledialog.askstring("Failure", "Disable which city?")
        if node in self.graph:
            self.graph.remove_node(node)
            self.status.config(text=f"Node failed: {node}")
            self.draw_graph(title=f"Node {node} Failed")


    # Graph coloring

    def graph_coloring(self):
        colors = nx.coloring.greedy_color(self.graph)
        color_map = []

        for node in self.graph:
            color_map.append(
                ["#e74c3c", "#3498db", "#2ecc71", "#f1c40f"][colors[node] % 4]
            )

        self.ax.clear()
        pos = nx.spring_layout(self.graph, seed=42)
        nx.draw(self.graph, pos,
                with_labels=True,
                node_color=color_map,
                node_size=700)
        self.ax.set_title("Graph Coloring (Frequency Assignment)", fontweight="bold")
        self.canvas.draw()


    # Command tree optimizer

    def command_tree(self):
        win = tk.Toplevel(self.root)
        win.title("Command Hierarchy Optimizer")
        win.geometry("700x400")

        canvas = tk.Canvas(win, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)

        def draw_before():
            canvas.delete("all")
            nodes = ["HQ", "A", "B", "C", "D"]
            y = 60
            for i, n in enumerate(nodes):
                canvas.create_oval(120, y-20, 160, y+20, fill="#f9e79f")
                canvas.create_text(140, y, text=n)
                if i > 0:
                    canvas.create_line(140, y-40, 140, y-20)
                y += 60
            canvas.create_text(140, 20, text="Before Optimization",
                               font=("Arial", 12, "bold"))

        def draw_after():
            canvas.delete("all")

            canvas.create_oval(350, 60, 390, 100, fill="#82e0aa")
            canvas.create_text(370, 80, text="HQ")

            canvas.create_oval(250, 160, 290, 200, fill="#aed6f1")
            canvas.create_oval(450, 160, 490, 200, fill="#aed6f1")
            canvas.create_text(270, 180, text="A")
            canvas.create_text(470, 180, text="B")

            canvas.create_oval(220, 260, 260, 300, fill="#d7bde2")
            canvas.create_oval(320, 260, 360, 300, fill="#d7bde2")
            canvas.create_text(240, 280, text="C")
            canvas.create_text(340, 280, text="D")

            canvas.create_line(370, 100, 270, 160)
            canvas.create_line(370, 100, 470, 160)
            canvas.create_line(270, 200, 240, 260)
            canvas.create_line(270, 200, 340, 260)

            canvas.create_text(370, 20, text="After Optimization",
                               font=("Arial", 12, "bold"))

        btn_frame = tk.Frame(win)
        btn_frame.pack(side=tk.BOTTOM, pady=10)

        tk.Button(btn_frame, text="Show Original",
                  command=draw_before).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Optimize",
                  command=draw_after).pack(side=tk.LEFT, padx=10)

        draw_before()




if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencyNetworkSimulator(root)
    root.mainloop()
