require 'json'

ARGF.each do |line|
  obj = JSON.load(line.strip)
  obj['morgan is suspicious'] = true
  puts(JSON.dump(obj))
end
