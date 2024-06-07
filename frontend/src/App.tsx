import { useState } from "react";
import "./App.css";
import { axios_instance } from "./api";
import { Loader } from "./loader";
import { Result } from "./Result";

function App() {
  const [file, setFile] = useState<File | undefined>(undefined);
  const [text, setText] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const postFile = async () => {
    if (!file) return;

    setText("");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios_instance.post(
        "/asr/upload_audio",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      const responseText = response.data.text;
      setText(responseText);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      <h1 className="mb4 lg:text-gray font-extrabold text-4xl mb-8">ASR</h1>
      <div id="inputs" className="mb-12">
        <input
          className="file-input file-input-bordered file-input-primary w-full max-w-xs"
          id="file-input"
          type="file"
          onChange={(e) => setFile(e.target.files?.[0])}
        />
        <button
          className="btn btn-primary"
          id="upload-button"
          onClick={postFile}
        >
          Загрузить
        </button>
      </div>
      {isLoading ? (
        <Loader />
      ) : text ? (
        <Result text={text as string} />
      ) : (
        <>Выберите файл для вывода текста</>
      )}
    </>
  );
}

export default App;

