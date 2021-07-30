from src.Kernel import Kernel

if __name__ == '__main__':
    try:
        kernel = Kernel()
        kernel.exec()
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exiting...")
        pass
