def main():
  n = int(input())
  m = int(input())

  gates_cards = {a: 0 for a in range(1, n + 1)}
  arrive_time = {}
  departure_time = {}
  summary = 0

  for _ in range(m):

      arrive, leave, enter, out = map(int, input().split())

      if arrive not in arrive_time:
          arrive_time[arrive] = [(arrive, enter)]
      else:
          arrive_time[arrive].append((arrive, enter))

      if leave not in departure_time:
          departure_time[leave] = [(leave, out)]
      else:
          departure_time[leave].append((leave, out))

  for i in range(6, 23):

      if i in departure_time:

          for j in departure_time[i]:
              gates_cards[j[1]] += 1

      if i in arrive_time:

          for j in arrive_time[i]:

              if gates_cards[j[1]] == 0:
                  summary += 1
              else:
                  gates_cards[j[1]] -= 1

  print(summary)
  
  
if __name__ == '__main__':
    main()
