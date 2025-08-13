# ---------- w mode ----------
print("---- Writing to file (w mode) ----")
f = open("sample.txt", "w")
f.write("Line 1: DKTE-TEI-Ich-ETC-Dept.\n")
f.write("Line 2: Electronics & Telecommunication\n")
f.write("Line 3: Python File Handling Example\n")
f.close()
print("Data written in 'w' mode.\n")

# ---------- r mode ----------
print("---- Reading file (r mode) ----")
f = open("sample.txt", "r")
print(f.read())
f.close()

# ---------- a mode ----------
print("---- Appending data (a mode) ----")
f = open("sample.txt", "a")
f.write("Line 4: This line is appended using 'a' mode.\n")
f.close()
print("Data appended.\n")

# ---------- r+ mode ----------
print("---- Read and Write (r+ mode) ----")
f = open("sample.txt", "r+")
content = f.read()
print("Before writing in r+ mode:\n", content)
f.seek(0)  
f.write("UPDATED LINE 1 (using r+ mode)\n")
f.close()
print("File updated with r+ mode.\n")

# ---------- w+ mode ----------
print("---- Write and Read (w+ mode) ----")
f = open("sample_wplus.txt", "w+")
f.write("This file is written using w+ mode.\n")
f.write("Existing content is overwritten in w+.\n")
f.seek(0)  
print(f.read())
f.close()

# ---------- a+ mode ----------
print("---- Append and Read (a+ mode) ----")
f = open("sample_aplus.txt", "a+")
f.write("This file is written using a+ mode.\n")
f.seek(0)  
print(f.read())
f.close()
