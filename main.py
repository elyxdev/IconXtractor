import icoextract
import sys, os

def extract_icon(exe_path, output_path="icono.ico"):
    extractor = icoextract.IconExtractor(exe_path)
    if output_path == "icono.ico":
        output_path = os.path.basename(exe_path).replace(".exe", ".ico")
    extractor.export_icon(output_path)
    print(f"Icono guardado en: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("<entrada.exe> [salida.ico]")
        sys.exit(1)
    exe_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "icono.ico"
    extract_icon(exe_file, output_file)