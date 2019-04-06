declare @row int = 1
while (@row < 21)
begin
    print replicate('* ', @row)
    set @row = @row + 1
end