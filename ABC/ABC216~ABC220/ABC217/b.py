def main():
    all_sets = set(['ABC', 'ARC', 'AGC', 'AHC'])
    input_sets = set([input() for _ in range(3)])
    
    print(list(all_sets - input_sets)[0])

if __name__ == '__main__':
    main()
