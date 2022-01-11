procedure romnum(local_num, rank:integer);
begin
  var romnums:string;
  romnums := 'IVXLCDM';
  case local_num of
    1..3: write(romnums[rank] * local_num);
    4:    write(romnums[rank] + romnums[rank+1]);
    5..8: write(romnums[rank+1] + romnums[rank] * (local_num - 5));
    9:    write(romnums[rank] + romnums[rank+2]);
  end;
end;

procedure translate(num:integer);
var strnum: string;single_num, pascalgovno :integer;
begin
  str(num, strnum);
  for var i := 1 to length(strnum) do
  begin
    val(strnum[i], single_num, pascalgovno);
    romnum(single_num, (length(strnum)*2 + 1) - i*2);
  end;
  writeln();
end;
begin
  translate(3999);
  translate(3465);
  translate(34);
  translate(435);
  translate(1023);
end.


