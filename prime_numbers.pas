program prime_numbers; //https://sun9-86.userapi.com/impg/swhhS1vKHpDD1k7VB3wI2ZW9X1q8j7vTbcXwaA/LScy66PngSY.jpg?size=1600x720&quality=96&sign=ce114e4e93648c4cc95a4c5ff0ef3d2f&type=album

uses
    LazUtf8;


function is_prime(num:integer):Boolean;
var i:Integer;
begin
  if num = 1 then
  begin
    is_prime := true;
    exit;
  end;
  for i := 2 to num - 1 do
      if num mod i = 0 then
      begin
        is_prime := True;
        exit;
      end;
  is_prime := False;
end;

procedure find_prime(N:integer);
var i:Integer;
begin
  for i := 1 to N do
  begin
    if is_prime(i) then
      writeln(utf8toconsole(i, ' - простое число'));
  end;
  
end;


function getUTF8char(const s:string; var index:integer):string;
 var utf8char:array[1..6]of char=(#128,#224,#240,#248,#252,#254);
 var c,cid:char; i:byte;
begin
 result:='';
 if index>length(s) then exit;
 cid:=s[index];
 for i:=1 to 6 do begin
  c:=s[index]; inc(index); result:=result+c;
  if cid<utf8char[i] then exit;
 end;
end;

const rus='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ';

var ruscnt:array[1..66]of integer;
    s:string; i:integer;
    index:integer=1;
    symbol:string;
begin
 fillchar(ruscnt,sizeof(ruscnt),#0);
 write('введите строку: '); readln(s);
 while true do begin
  symbol:=getUTF8char(s,index);
  if symbol='' then break;
  if length(symbol)<>2 then continue;
  for i:=1 to 66 do if symbol=copy(rus,i*2-1,2) then inc(ruscnt[i]);
 end;
 for i:=1 to 66 do
  if ruscnt[i]=0 then continue
  else writeln (copy(rus,i*2-1,2),' - ',ruscnt[i]);
end.






// begin
//   find_prime(10)
// end.