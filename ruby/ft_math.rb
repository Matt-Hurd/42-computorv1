def baby_sqrt(number)
  if not number
    return 0
  end
  n = number / 2.0
  n2 = n + 1
  while (n != n2)
    x = number / n
    n2 = n
    n = (n + x) / 2
  end
  return n
end

puts baby_sqrt(4)