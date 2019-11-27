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
A,E,L,U
A,E,L,V
A,E,M,W
A,F,N,X
B,G,O,Y
B,G,P,Z
B,H,Q,Z
C,I,R,Z
C,J,S,Z
D,K,T,Z
```

### Output
```
A:
  E: {L: V, M: W}
  F: {N: X}
B:
  G: {O: Y, P: Z}
  H: {Q: Z}
C:
  I: {R: Z}
  J: {S: Z}
D:
  K: {T: Z}
```

