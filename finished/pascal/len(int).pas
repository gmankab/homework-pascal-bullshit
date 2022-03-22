function len(num:integer):integer; // находит длину числа без использования строк
var answer:integer;
begin
  while num <> 0 do //делим на 10 пока число не кончится
  begin
    num := num div 10;
    answer := answer + 1;
  end;
  len := answer
end;

begin
var a:integer;
readln(a);
writeln(len(a));
end.

  