# Speech to text модель

Запуск:

```
eval "$($HOME/anaconda3/bin/conda shell.bash hook)"
conda activate nemo
python3 asr/server.py &
cd frontend && npm run dev &
cd ..
```
