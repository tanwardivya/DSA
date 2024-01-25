class DailyTemperature:
    def daily_temperature(self,temperatures:list[int])->list[int]:
        result = [0] * len(temperatures)
        stack = [] #pair: [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackInd = stack.pop()
                result[stackInd] = i-stackInd
            stack.append((t,i))
        return result

def main():
    dt = DailyTemperature()
    result = dt.daily_temperature([73,74,75,71,69,72,76,73])
    print(result)

if __name__ =="__main__":
    main()

