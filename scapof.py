import argparse
from src.spoofing_engine import SpoofingEngine

def banner():
    print(r"""


                  ~!               :?             
                  ~GY!:.^~~~~~^:.^?GY             
               :^^~5GG5Y55YYYY5YYPGP^             
              .JYYYY5Y?!^:...:^~?Y5Y7.            
   ^!^ ^!!!!!!!!7JY5?:           :7Y5J:           
   ?Y?.?YYYJJJJJYYY7               ~Y5J.          
    .   ...!????YYY.          ^7!^. ?Y5!          
           7JJJJYYY.          !Y55J!?Y5!          
                ?YY!           .:7Y5YYY:          
                !5YY7.            :JYY?           
               .YYYY5Y7^.          .YYY^          
         .:::::~YYJ:!JY5J.          ?55!          
        .JYYYYYYYYY:  :^:          .JY5^          
         .:!7~:!JYYJ:             .?55?           
          .JY!.JYYY5Y!:         .~J5Y7.           
           ..  ...:7Y55J7!~~~~7JY5Y?^             
                    .^!?JYYYYYJJ7~.               
                  ::..:..~^:~^:.:: !?.            
                  7J!J!^!?Y^Y~J7?77?!             
                  .:..:.::::7::.::.:.             


    """)


def parse_args():
    parser = argparse.ArgumentParser(description="Scapof - A CLI-based ARP Spoofing tool.")

    parser.add_argument(
        "-sm", "--src-mac", required=True, help="Source MAC address (e.g., 00:11:22:33:44:55)"
    )
    parser.add_argument(
        "-dm", "--dst-mac", required=True, help="Destination MAC address (e.g., ff:ff:ff:ff:ff:ff)"
    )
    parser.add_argument(
        "-si", "--src-ip", required=True, help="Source IP address (e.g., 192.168.1.100)"
    )
    parser.add_argument(
        "-di", "--dst-ip", required=True, help="Destination IP address (e.g., 192.168.1.1)"
    )
    parser.add_argument(
        "--op", type=int, choices=[1, 2], default=1, help="ARP Operation type: 1 for request, 2 for reply (default: 1)"
    )
    parser.add_argument(
        "--con", action="store_true", help="Send ARP replies indefinitely"
    )

    return parser.parse_args()


def main():
    banner()

    # Parse command-line arguments
    args = parse_args()

    # Print the user's inputs for confirmation
    print(f"Source MAC: {args.src_mac}")
    print(f"Destination MAC: {args.dst_mac}")
    print(f"Source IP: {args.src_ip}")
    print(f"Destination IP: {args.dst_ip}")
    print(f"ARP Operation: {'Request' if args.op == 1 else 'Reply'}")
    print(f"Continuous Sending: {'Enabled' if args.con else 'Disabled'}")

    # Initialize the Spoofing Engine
    engine = SpoofingEngine()

    try:
        if args.con:
            while True:
                engine.send_arp_spoof(
                    src_mac=args.src_mac,
                    dst_mac=args.dst_mac,
                    src_ip=args.src_ip,
                    dst_ip=args.dst_ip,
                    op=args.op
                )

        else:
            # Send a single ARP spoof packet
            engine.send_arp_spoof(
                src_mac=args.src_mac,
                dst_mac=args.dst_mac,
                src_ip=args.src_ip,
                dst_ip=args.dst_ip,
                op=args.op
            )
            print("ARP packet successfully sent.")

    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nTerminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
