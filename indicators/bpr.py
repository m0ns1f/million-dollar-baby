from ict_smc import smc

def detect_bpr(ohlc: pd.DataFrame):
    """
    Identifies Balanced Price Ranges (BPR), Fair Value Gaps (FVG), and Inverted Fair Value Gaps (IFVG)
    using the smartmoneyconcepts library.
    
    Parameters:
        ohlc (pd.DataFrame): DataFrame with columns ['open', 'high', 'low', 'close', 'volume']

    Returns:
        pd.DataFrame: Original DataFrame with additional columns for BPR, FVG, and IFVG detection
    """
    ohlc = ohlc.copy()
    
    # Identify Fair Value Gaps (FVG)
    fvg_data = smc.fvg(ohlc, join_consecutive=True)
    ohlc['FVG'] = fvg_data['fvg']
    
    # Identify Inverted Fair Value Gaps (IFVG)
    ohlc['IFVG'] = ohlc['FVG'] * -1  # Simple inversion for demonstration
    
    # Identify Balanced Price Range (BPR) using liquidity method
    liquidity_data = smc.liquidity(ohlc, range_percent=0.02, up_thresh=0.05, down_thresh=-0.05)
    ohlc['BPR'] = liquidity_data['liquidity']
    return ohlc