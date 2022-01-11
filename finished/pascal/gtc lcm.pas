function gtk(num1, num2:integer):integer; // находит наибольший общий делитель
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

function lcm(num1, num2:integer):integer; // наименьшее общее кратное
begin
  lcm := (num1 * num2) div gtk(num1, num2);
end;

begin
var a, b:integer;
readln(a, b);
writeln(gtk(a, b));
writeln(lcm(a, b));
end.
  