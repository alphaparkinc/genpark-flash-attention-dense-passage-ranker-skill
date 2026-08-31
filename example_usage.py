from client import FlashAttentionDensePassageRankerClient

def main():
    client = FlashAttentionDensePassageRankerClient()
    res = client.rank_passages('Zero-knowledge proof verification gas cost on Ethereum L2 rollups', 50, 3)
    print('FlashAttention Dense Ranker: ' + res['ranking_session_id'])
    print('Throughput: ' + str(res['throughput_passages_per_sec']) + ' passages/s | Flash Attention: ' + str(res['flash_attention_kernel_accelerated']))
    print('Top Passage: ' + res['top_scoring_passage_id'])

if __name__ == '__main__':
    main()
