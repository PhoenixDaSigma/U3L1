# Phoenix Valent
  # U3L1
    # Prove that while loops are better than recursion

def recursionExample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    recursionExample(num-1)
    print(f"Returning; num = {num}")
    return

def whileLoopUser(num):
  firstNum = num

  while num > 0:
    print(f"Recursing; num = {num}")
    num-=1
  print("\nBASE CASE REACHED\n")
  while num < firstNum:
    num+=1
    print(f"Returning; num = {num}")


def main():
  print("Recursion:")
  recursionExample(5)
  print("<>"*10)
  print("Loopz:")
  whileLoopUser(5)

if __name__ == "__main__":
  main()