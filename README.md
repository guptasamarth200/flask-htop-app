# Flask App with `/htop` Endpoint

This is a simple Flask application that exposes an `/htop` endpoint, displaying system information such as:

- Your full name
- System username
- Server time in IST
- Output of the `top` command

## 🚀 Setup and Run the App

### **1. Start GitHub Codespace**
- Open GitHub and create a new Codespace from your repository.
- Wait for the Codespace environment to load.

### **2. Install Dependencies**
Run the following command in the **Codespace terminal** to install Flask:

```bash
pip install flask
```

### **3. Run the Flask App**
Start the Flask application using:

```bash
python app.py --host=0.0.0.0 --port=8080
```

> If port `8080` is busy, use `5500` or `3000` instead.

### **4. Expose the Port**
- Open the **"Ports" tab** in GitHub Codespaces.
- Look for **Port 8080** (or the port you used).
- If not listed, click **"+ Add Port"**, enter `8080`, and set **visibility to Public**.

### **5. Access the `/htop` Endpoint**
Once the app is running:
- Copy the **public URL** from the **Ports tab**.
- Open an **Incognito tab** and visit:

  ```
  https://your-codespace-url.github.dev/htop
  ```

### **6. Example Output**
Your `/htop` endpoint should display:

```html
<h1>System Info</h1>
<p>Name: Samarth Gupta</p>
<p>Username: your-system-username</p>
<p>Server Time (IST): 2025-02-18 14:30:00</p>
<pre>
top - 14:30:00 up 10 days,  5:40,  2 users,  load average: 0.75, 0.80, 0.65
Tasks: 150 total,   1 running, 149 sleeping,   0 stopped,   0 zombie
Cpu(s):  5.0%us,  2.0%sy,  0.0%ni, 92.0%id,  1.0%wa,  0.0%hi,  0.0%si,  0.0%st
Mem:   4096MB total,  2000MB used,  2096MB free,   512MB buffers
</pre>
```

### **7. Submitting the Test**
For submission:
- **Link 1:** `https://your-codespace-url.github.dev/htop`
- **Link 2:** GitHub repository link (`https://github.com/your-repo`)

## 🛠 Troubleshooting
### **If you see "404 Not Found"**
- Ensure the Flask app is running.
- Check if the port is **exposed and set to Public** in the **Ports tab**.
- Restart the app and use `8080`, `5500`, or `3000`.

### **If the URL doesn’t work**
- Try opening in an **Incognito Tab**.
- Ensure the Codespace is running and hasn’t timed out.
- Use `gh codespace ports visibility 8080:public -c $CODESPACE_NAME` to manually set the port visibility.

---

## 📌 Notes
- **Do not stop the Codespace**, as the endpoint should remain live.
- If your Codespace stops, restart it and re-run `python app.py`.

Happy coding! 🚀