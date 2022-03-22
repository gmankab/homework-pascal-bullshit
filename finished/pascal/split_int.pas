program split_int;

procedure nums();
begin
  var num, num2:integer;
  var factor:real;
  readln (num);
  num2 := num;
  factor := 1;
  while num <> 0 do
  begin
    num := num div 10;
    factor := factor * 10;
  end;
  while factor <> 1 do
  begin
    factor := factor / 10;
    writeln(num2 div trunc(factor));
    num2 := num2 mod trunc(factor)
  end;
  
end;
begin
  nums()
end.