csv2yaml
========
Convert CSV to (nested) YAML

## Installation

```bash
$ git clone https://github.com/yh549848/csv2yaml.git
$ cd csv2yaml && python setup.py install
```

## Usage

```bash
$ csv2yaml <csv> >| output.yaml
```

## Example
### Input

```
A,D,H,M,R
A,D,I,N,S
A,E,H,O,T
B,F,K,P,U
C,G,L,Q,V
```

### Output
```
A:
  D:
    H: {M: R}
    I: {N: S}
  E:
    H: {O: T}
B:
  F:
    K: {P: U}
C:
  G:
    L: {Q: V}
```