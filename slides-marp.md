---
theme: default
header: 'National Institute of Standards and Technology'
footer: 'Walter Rowe'
paginate: true
_paginate: false

---

# Title
### Subtitle

---
<!-- backgroundImage: "linear-gradient(to bottom, #cccccc, #999999)" -->

# Slide 1 Title

[Link to Marp Site](https://marp.app/)

Topic 1
- bullet 1
- bullet 2

centered

right aligned

---

# Slide 2 Title

Topic 2
- bullet 1
- bullet 2

more code below

```python
machines = {
    't2.small'  : { 'cpu':1, 'ram':2 },
    't2.medium' : { 'cpu':2, 'ram':4 },
    't2.large'  : { 'cpu':4, 'ram':8 }
}

for size in machines:
    print ("Machine Size",size,"has",machines[size]['cpu'],"CPUs and",machines[size]['ram'],"GB RAM")
```
