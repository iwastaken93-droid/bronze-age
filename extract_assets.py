import os
import UnityPy

def extract_assets(file_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    env = UnityPy.load(file_path)

    for obj in env.objects:
        if obj.type.name == "TextAsset":
            data = obj.read()
            name = getattr(data, 'm_Name', str(obj.path_id))
            out_path = os.path.join(output_dir, f"{name}.txt")
            script_data = getattr(data, 'script', getattr(data, 'm_Script', b''))
            if isinstance(script_data, str):
                script_data = script_data.encode('utf-8')
            with open(out_path, "wb") as f:
                f.write(bytes(script_data))

extract_assets("extracted/data.unity3d", "extracted_assets")
