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


function reverse_number(num:integer):integer;
var answer, rank2:integer;
begin
  rank2 := rank(num); // rank это разряд, например в цифре 1234 у двойки разряд тысячи,а у четверки единицы
  while rank2 <> 1 do 
  begin
    answer := answer + (num mod 10)*rank2; // вставляем в ответ цифру на место ее разряда
    num := num div 10;
    rank2 := rank2 div 10; // делим эту хрень (rank) на 10 пока она не сравняется с нулем
    writeln('считаем: ', answer, ' + ', (num mod 10)*rank2, ' = ', answer + (num mod 10)*rank2, '; rank = ', rank2);
    //эта строчка с writeln не влияет на работу функции, она нужна только чтобы было понятнее как код работает
  end;
  reverse_number := answer
end;


begin
var a:integer;
readln(a);
writeln(reverse_number(a));
end.
  