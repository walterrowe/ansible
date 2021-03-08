name: title
class: middle,center

# Title

### Subtitle

---
name: content

# Slide 1 Title

.left[

[Link to RemarkJS Wiki](https://github.com/gnab/remark/wiki)

Topic 1
- bullet 1
- bullet 2

.center[
centered
]

.right[
right aligned
]

]

???
Presenter notes go here and are not visible in the slide show presentation.

---
class: center
# Slide 2 Title

.left[

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

]
