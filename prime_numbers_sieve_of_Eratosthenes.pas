program prime_numbers_sieve_of_Eratosthenes;
const
    N = 100;

var
    i, k:integer;
    A: array[2..N] of boolean;


begin
    for i := 2 to N do
      a[i] := True;
    k := 2;
    while k * k <= N do
    begin
      if A[k] then
      begin
        i := k * k;
        while i <= n do
        begin
          A[i] := False;
          i := i + k;
        end;
      end;
      k := k + 1;
    end;
    WriteLn(A[8]);
    for i := 2 to N do
        if A[i] then
         WriteLn(i);
end.
