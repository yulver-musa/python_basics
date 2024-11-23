world_record = float(input())
distance = float(input())
seconds_per_m = float(input())

a = distance * seconds_per_m
delay = distance // 15
b = delay * 12.5
total_time = a + b
total_time = total_time
diff = total_time - world_record

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
