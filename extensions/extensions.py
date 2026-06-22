
yoo = input("File name: ")
yoo = yoo . strip()

match yoo:
    case "happy.jpg" | "happy.jpeg" | "zipper.jpg":
        print("image/jpeg")
    case "cs50.gif":
        print("image/gif")
    case "check.png":
        print("image/png")
    case "document.pdf" | "document.PDF" | "test.txt.pdf":
        print("application/pdf")
    case "plain.txt":
        print("text/plain")
    case "files.zip":
        print("application/zip")

    case _:
        print("application/octet-stream")
