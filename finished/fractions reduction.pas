function gtk(num1, num2:real):real; // находит наибольший общий делитель
begin
  while num1 <> num2 do
  begin
    if num1 > num2 then
      num1 := num1 - num2
    else
      num2 := num2 - num1;
  end;
  gtk := num1;
end;


procedure FracRed(num1, num2:real); //сокращает дробь a/b
begin
  (num1, num2) := (num1/gtk(num1, num2), num2/gtk(num1, num2));
  writeln (num1, ' ', num2)
end; 


begin
var a, b:integer;
readln(a, b);
FracRed(a, b);
end.
  