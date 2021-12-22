program prime_numbers_brute_force;
var
  actions_count:LongInt;
  prime_count:Integer;

function is_prime(num:integer):Boolean;
var
  i:Integer;
begin
  for i := 2 to num - 1 do
  begin
      actions_count := actions_count + 1;
      if num mod i = 0 then
      begin
        actions_count := actions_count + 1;
        is_prime := False;
        exit;
      end;
  end;
  actions_count := actions_count + 1;
  is_prime := True;
end;

procedure find_prime(N:integer);
var i:Integer;
begin
  for i := 2 to N do
  begin
    actions_count := actions_count + 1;
    if is_prime(i) then
    begin
      actions_count := actions_count + 1;
      prime_count := prime_count + 1;
    end;
  end;
end;


begin
  find_prime(10000);
  WriteLn('prime numbers count is ', prime_count);
  WriteLn('actions count is ', actions_count);
end.
