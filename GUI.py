import tkinter as tk
from tkinter import ttk
import MovieFinder
from tkinter import messagebox

def on_search_click():
    search_text = entry.get()
    if not search_text.strip():
        messagebox.showwarning("Empty Search", "Please enter a movie/TV show title")
        return
    
    search_button.config(state=tk.DISABLED, text="Searching...")
    root.update()  # Force UI update
    
    try:
        results = MovieFinder.get_options(search_text)
        results_box.delete(1.0, tk.END)
        results_box.insert(tk.END, '\n'.join(results))
    except Exception as e:
        messagebox.showerror("Error", f"Search failed: {str(e)}")
    finally:
        search_button.config(state=tk.NORMAL, text="SEARCH")

# Main window setup
root = tk.Tk()
root.title("Streaming Finder Pro")
root.geometry("720x520")
root.configure(bg="#f0f0f0")

# Custom font
custom_font = ("Segoe UI", 10)

# Header frame
header_frame = tk.Frame(root, bg="#2c3e50", height=80)
header_frame.pack(fill=tk.X)

tk.Label(header_frame, 
         text="Streaming Search Engine", 
         font=("Segoe UI", 16, "bold"), 
         fg="white", 
         bg="#2c3e50").pack(pady=20)

# Search frame
search_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
search_frame.pack(fill=tk.X)

# Modern entry with placeholder effect
entry = ttk.Entry(search_frame, 
                 font=custom_font, 
                 width=50)
entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

# Modern button with hover effect
style = ttk.Style()
style.configure("TButton", 
               font=custom_font,
               padding=6,
               background="#3498db",
               foreground="black")

search_button = ttk.Button(search_frame, 
                         text="SEARCH", 
                         command=on_search_click,
                         style="TButton")
search_button.pack(side=tk.RIGHT)

# Results frame
results_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=10)
results_frame.pack(fill=tk.BOTH, expand=True)

# Scrollable results box
scrollbar = tk.Scrollbar(results_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_box = tk.Text(results_frame, 
                     wrap=tk.WORD,
                     font=custom_font,
                     yscrollcommand=scrollbar.set,
                     padx=10,
                     pady=10,
                     bg="white",
                     relief=tk.FLAT)
results_box.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=results_box.yview)

# Footer
footer_frame = tk.Frame(root, bg="#2c3e50", height=30)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
tk.Label(footer_frame, 
        text="© 2023 Streaming Finder", 
        fg="white", 
        bg="#2c3e50",
        font=("Segoe UI", 8)).pack(pady=5)

# Focus on entry when app starts
entry.focus_set()

# Bind Enter key to search
root.bind('<Return>', lambda event: on_search_click())

root.mainloop()