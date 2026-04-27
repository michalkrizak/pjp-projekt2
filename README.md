# PJP Projekt

## 1. Virtuální prostředí

```bash
# Aktivace (venv je sdílený z nadřazené složky)
source ~/vsb/pjp/venv/bin/activate

# Instalace závislostí (jen poprvé)
pip install antlr4-python3-runtime==4.13.2
```

## 2. Generování parseru z gramatiky

Spustit po každé změně `PJP.g4`:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor PJP.g4
```

Vygeneruje: `PJPLexer.py`, `PJPParser.py`, `PJPVisitor.py`

## 3. Spuštění

```bash
# Kompilace zdrojového kódu → vygeneruje .instr soubor
python compiler.py sampleInputs/SampleInput1.txt

# Spuštění vygenerovaných instrukcí
python interpreter.py sampleInputs/SampleInput1.instr
```

## 4. Tok programu

```
zdrojový kód (.txt)
    → compiler.py  → instrukce (.instr)
    → interpreter.py → výstup
```

  - ? = volitelné (0 nebo 1×)
  - * = nula nebo vícekrát
  - + = jednou nebo vícekrát