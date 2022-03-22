program prime_numbers_sieve_of_Eratosthenes;
const
  N = 10000;

var
  i, k:integer;
  A: array[2..N] of boolean;
  actions_count:LongInt;
  prime_count:Integer;


begin
  for i := 2 to N do
  begin
    actions_count := actions_count + 1;
    a[i] := True;
  end;
  k := 2;
  while k * k <= N do
  begin
    actions_count := actions_count + 1;
    if A[k] then
    begin
      actions_count := actions_count + 1;
      i := k * k;
      while i <= n do
      begin
        actions_count := actions_count + 1;
        A[i] := False;
        actions_count := actions_count + 1;
        i := i + k;
      end;
    end;
    actions_count := actions_count + 1;
    k := k + 1;
  end;
  for i := 2 to N do
  begin
    actions_count := actions_count + 1;
    if A[i] then
    begin
      actions_count := actions_count + 1;
      prime_count := prime_count + 1;
    end;
  end;
  WriteLn('prime numbers count is ', prime_count);
  WriteLn('actions count is ', actions_count);
end.
