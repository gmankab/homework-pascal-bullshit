procedure lcm(num1, num2:integer); // находит наибольший общий делитель
var gtk1, gtk2:integer;
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
  writeln((num1 * num2) div gtk1); // умножаем 2 числа и делим на нод чтобы полчить нок
end;


begin
var a, b:integer;
readln(a, b);
lcm(a, b);
end.
  