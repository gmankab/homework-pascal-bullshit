program prime_numbers;
var actions_count:LongInt;

function is_prime(num:integer):Boolean;
var i:Integer;
begin
  actions_count := actions_count + 1;
  if num = 1 then
  begin
    is_prime := False;
    actions_count := actions_count + 1;
    exit;
  end;
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
  for i := 1 to N do
  begin
    actions_count := actions_count + 1;
    if is_prime(i) then
      writeLn(i, ' is prime');
  end;
end;


begin
  find_prime(10000);
  WriteLn('actions count is ', actions_count);
end.
