procedure FracRed(num1, num2:real); //сокращает дробь a/b
var gtk1, gtk2:real;
begin
  gtk1 := num1;
  gtk2 := num2;
  while gtk1 <> gtk2 do // находит наибольший общий делитель(gtk1)
  begin
    if gtk1 > gtk2 then
      gtk1 := gtk1 - gtk2
    else
      gtk2 := gtk2 - gtk1;
  end;

  num1 := num1/gtk1;
  num2 := num2/gtk1;
  writeln (num1, ' ', num2)
end; 


begin
var a, b:integer;
readln(a, b);
FracRed(a, b);
end.
  