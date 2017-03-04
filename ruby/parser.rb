def parse(equation_in)
  equation = equation_in.delete(' ')
  if (equation !~ /^(\d+(\*X(\^\d+){0,1}){0,1}[+=-]{0,1})+$/) 
    raise "Invalid Equation: #{equation_in}"
  end
end

parse("A")
