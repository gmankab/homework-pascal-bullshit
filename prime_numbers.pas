program prime_numbers;


function check_if_prime(num:integer):Boolean;
var i:Integer;
begin
  check_if_prime := False;
  for i := 2 to num - 1 do
      if num mod i = 0 then
        check_if_prime := True;
end;

begin
  writeln(check_if_prime())
end.