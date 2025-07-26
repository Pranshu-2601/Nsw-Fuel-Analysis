from pathlib import Path

studentid = Path(__file__).stem

def log(step, output_df=None, other=None):
    print(f"--------------- {step} ----------------")
    if other is not None:
        print(step, other)
    if output_df is not None:
        df = output_df.head(5).copy(True)
        for c in df.columns:
            df[c] = df[c].apply(lambda a: a[:20] if isinstance(a, str) else a)
        df.columns = [a[:10] + "..." for a in df.columns]
        print(df.to_string())
