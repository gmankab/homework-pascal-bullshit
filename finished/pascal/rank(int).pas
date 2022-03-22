function rank(num:integer):integer; // находит 10^len, len = длина числа
var answer:integer;
begin
  answer := 1;
  while num <> 0 do // пока число не кончится
  begin
    num := num div 10;// делим на 10 
    answer := answer * 10;// множим ответ на 10
  end;
  rank := answer
end;

begin
var a:integer;
readln(a);
writeln(rank(a));
end.

  