(1 .. 1000).each { |x| 
  (1 .. 1000).each { |y| 
    a = (x * y).to_s + x.to_s + y.to_s
    arr = a.split(//).sort.uniq

    if a.size == 9 and arr.size == 9 and !arr.include?("0") then
      puts x.to_s + " " + y.to_s + " " + (x * y).to_s
    end
  }
}
