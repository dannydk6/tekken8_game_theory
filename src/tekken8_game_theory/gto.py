"""Code for creating GTO Distributions."""

import pandas as pd
import pygambit as gbt

from .utils import round_float, full_path

def create_gto_distribution(gbt_filename, base_path=None, precision=2, drop_zeros=False, no_prec_percent=False):
    """
    Converts a number (1-26) to its corresponding letter in the English alphabet.
    
    Args:
        gbt_filename (str): Filename for .gbt file being analyzed.
        base_path (str): Base directory where file is located.
        precision (int): Number of decimal places to round up to.
        drop_zeros (bool): Indicate whether to drop options with 0% distribution.
        
    Returns:
        df: DataFrame containing the players, strategies, and distributions.
        metadata: 
        
    Raises:
        ValueError: If the number is outside the range 1-26.
    """
    if not gbt_filename.endswith(".gbt"):
        raise ValueError("Only .gbt files are supported.")
    
    df = None
    metadata = {}
    path = full_path(gbt_filename, base_path)

    bt4 = gbt.Game.read_game(path)
    result = gbt.nash.lcp_solve(bt4)
    eqm = result.equilibria[0]
    
    players = [x.label for x in bt4.players]
    
    # Round payoff to number of decimals specified by precision
    payoff = round_float(float(eqm.payoff(players[0])), 1)
    
    # Get GTO distributions
    equilibria = []
    
    for player in players:
        for strategy, dist in eqm[player]:
            if drop_zeros and float(dist) == 0:
                continue
                
            # Get Strategy Distribution
            dist_r = round_float(100*float(dist), precision)
            dist_formatted = f"{dist_r}%"
            
            if no_prec_percent:
                dist_formatted = float(dist)
            
            # Get Strategy Payoff
            strat_val = float(eqm.strategy_value(strategy))
            strat_val_r = round_float(strat_val, precision)
            
            # Create row
            equilibria.append({"player": strategy.player.label,
                               "strategy": strategy.label,
                               "distribution": dist_formatted,
                               "strategy_value": strat_val_r})

    # Convert to pandas dataframe
    df = pd.DataFrame(equilibria)
    
    metadata = {
        "title": bt4.title,
        "P1": players[0],
        "P2": players[1],
        "Payoff": payoff, 
        "Comment": bt4.comment,
    }
    
    return df, metadata