# Playing with stdin / stdout aka pipes

We're going to serialize some data as json, and pass it through a few different languages, modifying the json as we go

```
python generate.py | node transform.js | ruby transform.rb | jq '.'
```
